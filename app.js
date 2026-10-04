(() => {
  'use strict';
  document.getElementById('year').textContent = new Date().getFullYear();
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const coarsePointer = matchMedia('(pointer: coarse)');
  const stage = document.getElementById('robot-stage');
  const robot = document.getElementById('robot');
  const pupils = document.querySelector('.robot-pupil');
  const head = document.getElementById('robot-head');
  const targetMarker = document.getElementById('tracking-target');
  const path = document.getElementById('tracking-path');
  const toggle = document.getElementById('motion-toggle');
  const instruction = document.getElementById('robot-instruction');
  let paused = reducedMotion.matches, frame = 0, lastTime = 0, visible = true;
  let x = 0, y = 0, targetX = 0, targetY = 0, gazeX = 0, gazeY = 0, eyeX = 0, eyeY = 0;
  const clamp = (n, min, max) => Math.max(min, Math.min(max, n));
  function render() {
    robot.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;
    pupils.style.transform = `translate(${eyeX}px, ${eyeY}px)`;
    head.style.transform = `rotate(${eyeX * .4}deg)`;
    const rect = stage.getBoundingClientRect();
    if (!rect.width || !rect.height) return;
    const sx = 250 + x / rect.width * 500, sy = 195 + y / rect.height * 390;
    const tx = 250 + targetX / rect.width * 500, ty = 195 + targetY / rect.height * 390;
    targetMarker.setAttribute('cx', tx.toFixed(2)); targetMarker.setAttribute('cy', ty.toFixed(2));
    path.setAttribute('d', `M${sx.toFixed(2)} ${sy.toFixed(2)} Q${((sx + tx) / 2).toFixed(2)} ${(sy - 20).toFixed(2)} ${tx.toFixed(2)} ${ty.toFixed(2)}`);
    targetMarker.style.opacity = Math.hypot(x-targetX,y-targetY) > 3 ? '.65' : '0';
  }
  function animate(now) {
    frame = 0;
    if(paused || !visible || document.hidden) return;
    const dt = lastTime ? Math.min((now-lastTime)/1000, .05) : 1/60;lastTime=now;
    const bodyEase=1-Math.exp(-5*dt), eyeEase=1-Math.exp(-12*dt);
    x+=(targetX-x)*bodyEase;y+=(targetY-y)*bodyEase;
    eyeX+=(gazeX-eyeX)*eyeEase;eyeY+=(gazeY-eyeY)*eyeEase;
    render();
    if(Math.abs(targetX-x)+Math.abs(targetY-y)+Math.abs(gazeX-eyeX)+Math.abs(gazeY-eyeY)>.06) frame=requestAnimationFrame(animate);
  }
  function start(){if(!paused && visible && !frame && !document.hidden){lastTime=0;frame=requestAnimationFrame(animate)}}
  function center(){targetX=targetY=gazeX=gazeY=0;start()}
  function guide(clientX,clientY){
    if(paused)return;
    const rect=stage.getBoundingClientRect();
    const localX=clientX-rect.left-rect.width/2, localY=clientY-rect.top-rect.height/2;
    gazeX=clamp((localX-x)/20,-10,10);gazeY=clamp((localY-y)/25,-7,7);
    // Keep the robot inside its own stage. Eyes can follow the pointer across the page.
    if(clientX>=rect.left && clientX<=rect.right && clientY>=rect.top && clientY<=rect.bottom){
      const maxX=Math.max(0,(rect.width-robot.offsetWidth)/2-16);
      const maxY=Math.max(0,(rect.height-robot.offsetHeight)/2-12);
      targetX=clamp(localX,maxX*-1,maxX);targetY=clamp(localY,maxY*-1,maxY);
    }
    start();
  }
  document.addEventListener('pointermove',e=>{if(e.pointerType!=='touch')guide(e.clientX,e.clientY)},{passive:true});
  stage.addEventListener('pointerdown',e=>guide(e.clientX,e.clientY),{passive:true});
  stage.addEventListener('keydown',e=>{
    const directions={ArrowLeft:[-30,0],ArrowRight:[30,0],ArrowUp:[0,-25],ArrowDown:[0,25]};
    if(paused || !directions[e.key])return;
    e.preventDefault();const [dx,dy]=directions[e.key],rect=stage.getBoundingClientRect();
    guide(rect.left+rect.width/2+targetX+dx,rect.top+rect.height/2+targetY+dy);
  });
  document.documentElement.addEventListener('pointerleave',center);
  function updateControls(){
    toggle.textContent=paused?'Enable tracking':'Pause tracking';toggle.setAttribute('aria-pressed',String(!paused));
    stage.parentElement.classList.toggle('paused',paused);
    instruction.textContent=paused?'Tracking paused.':coarsePointer.matches?'Tap around the robot to guide it.':'Move your pointer. I’m following.';
  }
  toggle.addEventListener('click',()=>{paused=!paused;updateControls();if(paused){cancelAnimationFrame(frame);frame=0}else start()});
  reducedMotion.addEventListener('change',()=>{paused=reducedMotion.matches;cancelAnimationFrame(frame);frame=0;if(paused){x=y=eyeX=eyeY=targetX=targetY=gazeX=gazeY=0;render()}updateControls();start()});
  coarsePointer.addEventListener('change',updateControls);
  new ResizeObserver(()=>{x=y=targetX=targetY=0;render()}).observe(stage);
  new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;if(!visible){cancelAnimationFrame(frame);frame=0}else start()}).observe(stage);
  document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);frame=0}else start()});
  document.getElementById('copy-email').addEventListener('click',async()=>{
    const status=document.getElementById('copy-status');
    try{await navigator.clipboard.writeText('aj4700@nyu.edu');status.textContent='Copied to clipboard.'}catch{status.textContent='Email: aj4700@nyu.edu'}
  });
  updateControls();render();
})();

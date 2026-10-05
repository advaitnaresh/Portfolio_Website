(() => {
 'use strict';
 document.getElementById('year').textContent=new Date().getFullYear();
 document.getElementById('copy-email')?.addEventListener('click',async()=>{const s=document.getElementById('copy-status');try{await navigator.clipboard.writeText('aj4700@nyu.edu');s.textContent='Copied.'}catch{s.textContent='aj4700@nyu.edu'}});
 const cards=[...document.querySelectorAll('#project-list .project')], search=document.getElementById('project-search');
 let category='All';
 function filter(){const query=search.value.trim().toLowerCase();let count=0;cards.forEach(card=>{const show=(category==='All'||card.dataset.category===category)&&card.textContent.toLowerCase().includes(query);card.hidden=!show;if(show)count++});document.getElementById('project-count').textContent=`${count} ${count===1?'project':'projects'}`;document.getElementById('no-results').hidden=count!==0}
 document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{category=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));filter()}));search?.addEventListener('input',filter);
 const cat=document.getElementById('cat'),direction=cat.querySelector('.cat-direction'),followInput=document.getElementById('cat-follow'),showInput=document.getElementById('cat-show'),mode=document.getElementById('cat-mode');
 const motion=matchMedia('(prefers-reduced-motion: reduce)'),fine=matchMedia('(pointer:fine)');
 const read=(key,fallback)=>{try{const v=localStorage.getItem(key);return v===null?fallback:v==='true'}catch{return fallback}};
 const save=(key,value)=>{try{localStorage.setItem(key,String(value))}catch{}};
 let following=read('portfolio.cat.follow',fine.matches&&!motion.matches),shown=read('portfolio.cat.show',true);
 let x=30,y=innerHeight-125,tx=x,ty=y,px=0,py=0,hasPointer=false,lastPointer=0,nextIdle=0,holdUntil=0,lastPounce=0,frame=0,lastTime=0;
 function state(value){if(cat.dataset.state!==value)cat.dataset.state=value}
 const clamp=(v,lo,hi)=>Math.min(Math.max(v,lo),Math.max(lo,hi));
 function bound(){const w=cat.offsetWidth||105,h=cat.offsetHeight||88;tx=clamp(tx,5,innerWidth-w-5);ty=clamp(ty,5,innerHeight-h-8);x=clamp(x,5,innerWidth-w-5);y=clamp(y,5,innerHeight-h-8)}
 function render(){cat.style.transform=`translate3d(${x.toFixed(1)}px,${y.toFixed(1)}px,0)`}
 function update(){followInput.checked=following;showInput.checked=shown;cat.hidden=!shown;mode.textContent=!shown?'The cat is hidden.':motion.matches?'Reduced motion: the cat is resting.':following?'Move your cursor. The cat will follow.':'The cat will wander, sit, and play.';if(shown&&!motion.matches)start();else{cancelAnimationFrame(frame);frame=0;state('sit')}}
 function idle(now){if(now<nextIdle)return;nextIdle=now+3000+Math.random()*3500;const choice=Math.random();if(choice<.4){tx=15+Math.random()*Math.max(0,innerWidth-150);ty=40+Math.random()*Math.max(0,innerHeight-180);bound();holdUntil=0}else{state(choice<.6?'sit':choice<.78?'groom':choice<.91?'play':'sleep');holdUntil=nextIdle}}
 function tick(now){frame=0;if(!shown||motion.matches||document.hidden)return;const dt=Math.min((now-(lastTime||now))/1000,.04);lastTime=now;
 const chasing=following&&hasPointer&&now-lastPointer<5000;
 if(chasing){tx=px-80;ty=py+18;bound();if(now>=holdUntil)holdUntil=0}else idle(now);
 const dx=tx-x,dy=ty-y,distance=Math.hypot(dx,dy);
 if(now>=holdUntil&&distance>3){const speed=chasing?Math.min(580,90+distance*2):65,step=Math.min(distance,speed*dt);x+=dx/distance*step;y+=dy/distance*step;direction.style.transform=dx<0?'scaleX(-1)':'scaleX(1)';state('walk')}
 else if(chasing&&now>=holdUntil){if(now-lastPounce>2400&&now-lastPointer<1200){state('pounce');holdUntil=now+600;lastPounce=now}else state('sit')}
 render();frame=requestAnimationFrame(tick)}
 function start(){if(!frame&&shown&&!motion.matches&&!document.hidden){lastTime=0;frame=requestAnimationFrame(tick)}}
 document.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;px=e.clientX;py=e.clientY;hasPointer=true;lastPointer=performance.now();if(following&&cat.dataset.state!=='pounce')holdUntil=0;start()},{passive:true});
 document.documentElement.addEventListener('pointerleave',()=>{hasPointer=false;nextIdle=0});
 followInput.addEventListener('change',()=>{following=followInput.checked;save('portfolio.cat.follow',following);nextIdle=0;holdUntil=0;tx=x;ty=y;update()});
 showInput.addEventListener('change',()=>{shown=showInput.checked;save('portfolio.cat.show',shown);update()});
 addEventListener('resize',()=>{bound();render()});document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);frame=0}else start()});motion.addEventListener('change',update);
 bound();render();update();
})();

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor
import shutil,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf/Advait_Jishnani_Resume.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
W,H=612,792;M=16;WIDTH=W-2*M;TARGET=H*.96
styles={
 'body':ParagraphStyle('body',fontName='Times-Roman',fontSize=10,leading=11.7,textColor=HexColor('#151515')),
 'bullet':ParagraphStyle('bullet',fontName='Times-Roman',fontSize=10,leading=11.7,leftIndent=9,firstLineIndent=-7),
 'title':ParagraphStyle('title',fontName='Times-Bold',fontSize=20,leading=23,alignment=1),
 'contact':ParagraphStyle('contact',fontName='Times-Roman',fontSize=9,leading=11,alignment=1),
 'heading':ParagraphStyle('heading',fontName='Times-Bold',fontSize=11,leading=14),
}
items=[]
def p(text,kind='body',gap=2):
 a=Paragraph(text,styles[kind]);_,h=a.wrap(WIDTH,1000);items.append((a,h,gap,kind))
def section(t):p(t,'heading',4)
def role(title,date,org,location):
 p(f'<b>{title}</b> <font color="#555555">| {date}</font>',gap=1)
 p(f'<i>{org} | {location}</i>',gap=2)
def bullet(t):p('• '+t,'bullet',2)
p('Advait Jishnani','title',3)
p('New York, NY | +1 (646) 541-9891 | <link href="mailto:advaitnaresh@gmail.com">advaitnaresh@gmail.com</link>','contact',1)
p('<link href="https://linkedin.com/in/advait-jishnani">linkedin.com/in/advait-jishnani</link> | <link href="https://github.com/advaitnaresh">github.com/advaitnaresh</link>','contact',5)
section('EDUCATION')
p('<b>New York University</b> | M.S. Computer Science | Sep 2025 - May 2027',gap=2)
p('New York, NY | GPA: 4.0/4.0',gap=3)
p('<b>BITS Pilani, Goa</b> | B.E. Computer Science, Minor in Finance | Aug 2020 - May 2024',gap=2)
p('Goa, India | GPA: 4.0/4.0',gap=5)
section('EXPERIENCE')
role('Salesforce Assistant','Dec 2025 - Present','NYU','New York, NY')
bullet('Rebuilt Stripe payment and enrollment workflows with Salesforce Flow, supporting student onboarding across NYU courses generating $300K+ in revenue.')
bullet('Designed an Aura-based student site with reusable templates and embedded onboarding paths, from registration through course access.')
bullet('Integrated Salesforce, Stripe, and Brightspace through APIs and automated workflows, reducing manual handoffs and improving enrollment-data consistency.')
role('Data Engineering Intern','Jun 2026 - Aug 2026','Return on Creators','New York, NY')
bullet('Built an iMessage onboarding flow with Supabase and automated routing, designed to support up to 1,000 simultaneous creators.')
bullet('Developed mass messaging designed for 500 creators, accounting for load, failure cases, and backend reliability.')
bullet('Re-keyed a production messaging table with a composite key, rebuilt multi-line inbound routing, and resolved 3 data-integrity bugs before they reached the admin UI.')
role('Data Engineer','Jan 2024 - Aug 2025','Visa Inc.','Bengaluru, India')
bullet('Automated model-risk management and model refitting, cutting turnaround time by 60% and manual effort by 80%.')
bullet('Established data-quality validation across 15+ production models and orchestrated dependencies, retries, scheduling, and monitoring for 20+ Airflow workflows.')
bullet('Built large-scale Python, SQL, PySpark, and Hive transformations and supported Tableau reporting for 30+ stakeholders.')
role('Data Engineer Intern','May 2023 - Jun 2023','Visa Inc.','Bengaluru, India')
bullet('Reduced a production query from 2 hours to under 12 minutes through partitioning, caching, and bucketing in Hive and Spark.')
bullet('Investigated backend bottlenecks and schema-design trade-offs with senior engineers to improve analytical workloads.')
section('PROJECTS')
p('<b>Aries: Real-Time Data Platform</b> | Spark, Kafka, Python, PostgreSQL',gap=2)
bullet('Processed 10,000+ streaming events per second; served live KPIs at under 100 ms through tiered MinIO and PostgreSQL storage.')
p('<b>VulCAN: Automated Vulnerability Analyzer</b> | AWS Fargate, SQS, Python, PostgreSQL',gap=2)
bullet('Accelerated remediation workflows by 75% with an event-driven scanning service; decoupled 5,000+ daily jobs using SQS and Fargate.')
p('<b>RoCathon: Hybrid Creator Search</b> | PostgreSQL, pgvector, Gemini, TypeScript',gap=2)
bullet('Combined semantic retrieval, structured filters, and commerce-aware reranking to search 10,000+ creator profiles.')
bullet('Built JSON ingestion and embedding generation pipelines and used HNSW indexing for vector similarity retrieval.')
section('TECHNICAL SKILLS')
p('<b>Languages:</b> Python, SQL, Java, Bash. <b>Data:</b> Spark, PySpark, Kafka, Airflow, ETL/ELT, data modeling, data quality.',gap=1)
p('<b>Cloud &amp; tools:</b> AWS, GCP, PostgreSQL, Snowflake, Docker, Git/GitHub, CI/CD, Tableau.',gap=0)
content=sum(h for _,h,_,_ in items);gaps=sum(g for _,_,g,_ in items)
scale=(TARGET-content)/gaps
assert scale>=.2,(content,TARGET)
c=canvas.Canvas(str(OUT),pagesize=(W,H));c.setTitle('Advait Jishnani | Resume');c.setAuthor('Advait Jishnani')
y=H-M
for a,h,g,k in items:
 a.drawOn(c,M,y-h);y-=h
 if k=='heading':c.setStrokeColor(HexColor('#777777'));c.setLineWidth(.35);c.line(M,y-1,W-M,y-1)
 y-=g*scale
c.save();shutil.copy2(OUT,ROOT/'dist/resume.pdf')
print(json.dumps({'pages':1,'font_size':10,'page_height':H,'content_extent':round(TARGET,2),'page_fill_percent':96,'top_margin':M,'bottom_margin':round(y,2),'gap_scale':round(scale,2)}))


# Parse and structure all resume information for the portfolio website
resume_data = {
    "personal_info": {
        "name": "Advait Jishnani",
        "title": "Big Data Developer & ML Engineer",
        "tagline": "Building scalable data solutions and intelligent systems",
        "phone": "(646) 541-9891",
        "email": "aj4700@nyu.edu",
        "linkedin": "linkedin.com/in/advait-jishnani",
        "github": "github.com/advaitnaresh"
    },
    
    "education": [
        {
            "institution": "New York University",
            "degree": "Master of Science in Computer Science",
            "location": "New York, NY",
            "period": "Sep 2025 – May 2027",
            "status": "current"
        },
        {
            "institution": "Birla Institute of Technology and Science, Pilani",
            "degree": "Bachelor of Engineering in Computer Science",
            "minor": "Minor in Finance",
            "location": "Goa, India",
            "period": "Aug 2020 – May 2024",
            "status": "completed"
        }
    ],
    
    "technical_skills": {
        "Languages": ["Python (PySpark, Pandas, Scikit-learn)", "SQL", "C++", "Java", "Bash (Shell Scripting)"],
        "Technologies": ["Apache Spark", "Hadoop", "Hive", "Airflow", "Docker", "Kubernetes", "Git", "MongoDB", 
                        "Tableau", "ROS", "Kafka", "Terraform", "Snowflake", "Iceberg", "Advanced Prompt Engineering", 
                        "Github Copilot"],
        "ML & Cloud": ["AWS", "GCP", "MLOps (Model Deployment, Feature Engineering, CI/CD, Monitoring, Drift Detection)", 
                      "Model Risk Management (Data Governance)", "Data Modelling", "ETL/ELT", "Big Data Engineering"]
    },
    
    "certifications": ["Apache Iceberg", "Apache Airflow", "Spark", "Hive", "Intro to Trading", 
                      "ML & GCP", "Robotics", "Postman", "Python", "C++"],
    
    "work_experience": [
        {
            "title": "Associate Data Scientist",
            "company": "Visa Inc.",
            "location": "India",
            "period": "Jun 2024 – Aug 2025",
            "achievements": [
                "Led the VCTS2.0 solution as temporary team lead, architecting a unified MLOps pipeline that reduced the onboarding time for new regional models from 7 days to 3 days",
                "Engineered automated Model Risk Management (MRM) and Out-Of-Time (OOT) validation pipelines that cut manual effort by 80% while ensuring full regulatory compliance",
                "Delivered a 60% performance optimization in large-scale financial data workflows by spearheading the refactoring of a legacy Hive SQL codebase to PySpark",
                "Orchestrated the development of a universal automatic model refitting framework, scaling the solution from a single project to all production models and cutting refitting time from 7+days to 3 days"
            ],
            "metrics": {"onboarding_reduction": "57%", "manual_effort_reduction": "80%", "performance_optimization": "60%", "refitting_time_reduction": "57%"}
        },
        {
            "title": "Machine Learning Engineer Intern",
            "company": "Visa Inc.",
            "location": "India",
            "period": "Jan 2024 – Jun 2024",
            "achievements": [
                "Increased the operations team's efficiency by over 30% by engineering an end-to-end MLOps monitoring solution, which included the development of a real-time Tableau dashboard and a scalable Apache Airflow DAG to track all model workflows"
            ],
            "metrics": {"efficiency_increase": "30%"}
        },
        {
            "title": "Data Engineer Intern",
            "company": "Visa Inc.",
            "location": "India",
            "period": "May 2023 – Jul 2023",
            "achievements": [
                "Reduced a critical query's execution time by 98% (from 3 hours to 3 minutes) by identifying and implementing strategic optimizations in Hive, including partitioning, bucketing, and caching, which significantly expedited data availability for key stakeholders"
            ],
            "metrics": {"query_optimization": "98%"}
        }
    ],
    
    "projects": [
        {
            "name": "Optimal Trading Strategies using ARIMA & Reinforcement Learning",
            "technologies": ["Python", "ARIMA", "ML", "RL"],
            "description": "Achieved a 7% performance increase over a buy-and-hold benchmark by designing a hybrid ARIMA-RL trading algorithm that leveraged statistical forecasts to inform and optimize RL-driven trading policies",
            "impact": "7% performance increase"
        },
        {
            "name": "Model Predictive Control in Robot Operating System (ROS)",
            "technologies": ["ROS", "Gazebo", "TurtleBot 3"],
            "description": "Successfully implemented and deployed an optimized MPC controller in ROS, enabling a TurtleBot 3 to perform high-speed, real-time autonomous navigation and complex obstacle avoidance in simulated environments",
            "impact": "Real-time autonomous navigation"
        },
        {
            "name": "AI-Powered Applicant Tracking System (ATS)",
            "technologies": ["AWS", "Python", "MongoDB", "ML"],
            "description": "Architected and co-developed a cloud-based Applicant Tracking System (ATS) on AWS, which cut manual screening effort by 60% and accelerated the overall recruitment workflow by 60% by implementing an intelligent, ML-powered resume screening module and a Python/MongoDB backend",
            "impact": "60% reduction in manual effort"
        }
    ],
    
    "leadership": [
        {
            "title": "Roboficial Co-ordinator",
            "organization": "Quark BITS Pilani Goa",
            "location": "Goa, India",
            "period": "Sep 2022 – Apr 2023",
            "achievement": "Led a 140-person cross-functional team in organizing 6 national-level competitions, directing all logistics, communications, and rulebook creation while managing a budget of 60 lakh Rupees (approx. $72,000 USD) to attract 54 competing teams"
        }
    ],
    
    "key_metrics": {
        "onboarding_time_reduction": "57%",
        "manual_effort_reduction": "80%",
        "query_optimization": "98%",
        "performance_optimization": "60%",
        "efficiency_increase": "30%",
        "trading_performance": "7%",
        "ats_improvement": "60%",
        "team_size_led": "140",
        "budget_managed": "$72,000"
    }
}

# Print summary
print("Resume Data Extracted Successfully!")
print(f"\nName: {resume_data['personal_info']['name']}")
print(f"Current Education: {resume_data['education'][0]['institution']} - {resume_data['education'][0]['degree']}")
print(f"Total Work Experience Entries: {len(resume_data['work_experience'])}")
print(f"Total Projects: {len(resume_data['projects'])}")
print(f"Total Certifications: {len(resume_data['certifications'])}")
print(f"\nKey Skills Categories: {list(resume_data['technical_skills'].keys())}")
print(f"Total Skills: {sum(len(v) for v in resume_data['technical_skills'].values())}")


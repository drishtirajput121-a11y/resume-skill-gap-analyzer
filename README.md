# Resume Skill Gap Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Django-Framework-green?logo=django" />
  <img src="https://img.shields.io/badge/Python-Backend-blue?logo=python" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql" />
</p>

<p align="center">
  <b>An intelligent web application that analyzes resumes and identifies missing skills required for a target role.</b>
</p>


## Project Overview

Resume Skill Gap Analyzer is a Django-based web application that:

- Allows users to upload resumes
- Extracts existing skills
- Compares them with required skills
- Identifies missing skills (Skill Gap)
- Displays insights in a dashboard

This project helps students and job seekers understand what skills they need to improve.



## Tech Stack

- Backend: Python
- Framework: Django
- Database: PostgreSQL
- Frontend: HTML, CSS, Bootstrap
- Version Control: Git & GitHub


## Key Features

✔ User Authentication (Login System)  
✔ Resume Upload (PDF Support)  
✔ Skill Extraction  
✔ Skill Gap Analysis  
✔ Dashboard Visualization  
✔ Clean and Responsive UI  


# Application Screenshots



## 1️⃣ Login Page

![Login Page](images/login.gif)



## 2️⃣ Resume Upload Page

![Upload Page](images/upload.png)



## 3️⃣ Skill Analysis Result

Shows:
- Skills You Have
- Skills You Should Have
- Missing Skills

![Skill Analysis](images/result.png)


## 4️⃣ Dashboard

Displays:
- Analysis Summary
- User Insights
- Skill Comparison Overview

![Dashboard](images/dashboard.png)


# ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/resume-skill-gap-analyzer.git
cd resume-skill-gap-analyzer
2️⃣ Create Virtual Environment
python -m venv venv
Activate:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Database
Update settings.py with PostgreSQL credentials.

Run:

python manage.py migrate
5️⃣ Run Server
python manage.py runserver
Open:

http://127.0.0.1:8000/
📂 Project Structure
resume-skill-gap-analyzer/
│
├── analyzer/
├── templates/
├── static/
├── manage.py
└── README.md
🚀 Future Improvements
AI-based advanced skill matching

Job role recommendation

Resume scoring system

API integration with job portals

Deployment on cloud platform

👩‍💻 Author
Drishti Rajput

Aspiring Software Engineer | Python & Django Developer

```

⭐ Show Your Support
If you like this project, please consider giving it a ⭐ on GitHub!


git add .
git commit -m "Added professional README with images"
git push

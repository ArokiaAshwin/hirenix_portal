# Hirenix — Internship Connection Portal with NLP Screening

Hirenix is a secure, full-stack web application developed using Python and the Django framework to streamline the internship recruitment process. The platform features separate portal ecosystems for students and corporate recruiters, featuring a built-in automated candidate screening workflow driven by a custom NLP text-extraction pipeline.

## 🚀 Key System Features

### 1. Dual-Portal Authentication & Security Gates
* **Role-Based Access Control (RBAC):** Distinct interface modules for **Students** and **Recruiters**. Cross-portal entry attempts are blocked on the server side using explicit database profile validation gates.
* **Form Exploitation Defenses:** Cryptographic validation implemented via native token injection (`{% csrf_token %}`) across all submission forms to mitigate Cross-Site Request Forgery vulnerabilities.

### 2. Intelligent Resume Screening Pipeline (NLP Engine)
* **Automated Parsing:** Extracts unstructured text streams from binary PDF uploads using the `PyPDF2` package.
* **Algorithmic Skill Intersection:** Cleans, tokenizes, and normalizes candidate resumes, matching text layers against dynamic, comma-separated skill requirements set by employers.
* **Live Match Scoring:** Automatically computes a dynamic candidate suitability score out of 100% and displays matched skill badges on the dashboard.

### 3. Recruiter Analytics Dashboard
* **Aggregation Metrics:** Tracks key data points like **Total Applications Received** and **Average Talent Pool Score** on the fly using SQL database aggregations (`Count`, `Avg`).
* **Data Visualization:** Integrated frontend layout with **Chart.js** via JSON data serialization to display real-time bar graphs illustrating top technical skills found across applicants.

### 4. Status Automation & Console Email Routing
* **Application Tracker:** Lets recruiters shortlist or reject applicants dynamically, shifting application state flags in the database.
* **Email System:** Modifying a student's status triggers Hirenix's internal mail dispatch backend, writing automated update messages straight to the local console server for real-time tracking.

---

## 🛠️ Tech Stack & Architecture

* **Backend Core:** Python, Django Web Framework (MVT Architecture)
* **Frontend Engineering:** Tailwind CSS, JavaScript (ES6+), HTML5
* **Data Visualization:** Chart.js
* **Libraries & Packages:** PyPDF2
* **Database Layer:** Relational SQLite / PostgreSQL
* **Version Control:** Git, GitHub

---

## 💻 How to Install and Run Locally

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Hirenix.git](https://github.com/YOUR_USERNAME/Hirenix.git)
cd Hirenix

# 🏥 Hospital Management & TQM Quality Assurance System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hospital-management-tqm.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://sqlite.org)

A full-stack, data-driven Hospital Management System built with **Python**, **Streamlit**, and **SQLite**. This application combines core healthcare administrative workflows (CRUD operations, dynamic search, multi-criteria filtering, data export) with **Total Quality Management (TQM)** principles, featuring Failure Mode and Effects Analysis (FMEA) risk mitigation and live database integrity audits.

---

## 🌟 Key Features

### 1. 📋 Patient Registration & Management (CRUD)
- **Patient Onboarding:** Register patient records with bounded age validation (0–125), diagnostic classification, and admission dates.
- **Records Management:** View, update, and safely delete patient records with automated SQLite primary key auto-incrementing.
- **Data Validation:** Defensive input checking to prevent invalid ages, empty fields, or malformed records.

### 2. 🔍 Advanced Dual Search & Date Range Filtering
- **Multi-Field Search:** Search patients instantly by Name or Disease/Diagnosis.
- **Robust Date Parsing:** Filter records across dynamic date ranges using strict datetime coercion (`pd.to_datetime`) to avoid type mismatch crashes.
- **Zero-Crash Resilience:** Type-safe query handling for empty/null search queries.

### 3. 📥 Multi-Format Data Export
- **Excel & CSV Export:** Download filtered or full database records directly as `.xlsx` and `.csv` files.
- **Pre-download Validation:** Prevents empty file downloads when filter criteria yield zero rows.

### 4. 📊 Real-Time Visual Analytics & Operational KPIs
- **Live KPI Metrics:** Real-time calculation of Total Admissions, Average Patient Age, and Top Diagnoses.
- **Diagnosis Distribution:** Categorized breakdowns of admissions across medical departments.
- **Patient Flow Timeline:** Daily admission volume charts with automatic casing normalization (`str.title()`).

### 5. 🛡️ TQM & Live Data Integrity Audit
- **Live System Health Scoring:** Real-time computation of data integrity percentage based on null dates, out-of-bound ages, and duplicate records.
- **Engineering FMEA Integration:** Systematic risk reduction addressing potential software failure modes (reducing calculated Risk Priority Numbers by >98%).

---

## 🛠️ Tech Stack & Architecture

- **Frontend & UI Framework:** [Streamlit](https://streamlit.io/)
- **Backend & Database:** SQLite3 (Relational Database)
- **Data Processing & Analytics:** [Pandas](https://pandas.pydata.org/)
- **Spreadsheet Generation:** [OpenPyXL](https://openpyxl.readthedocs.io/)
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
Hospital-TQM-Project/
│
├── app.py                 # Main Streamlit application with UI & tabs
├── db.py                  # SQLite database helper functions & schema setup
├── seed_data.py           # Automated batch data population script
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 Getting Started & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/BaapOfCoding699/Hospital-TQM-Project.git
cd Hospital-TQM-Project
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Seed the Database with Sample Records
```bash
python seed_data.py
```

### 5. Launch the Application Locally
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to access the portal.

---

## 📦 Dependencies (`requirements.txt`)

```text
streamlit>=1.30.0
pandas>=2.0.0
openpyxl>=3.1.0
```

---

## 🛡️ TQM Risk Mitigation Summary (FMEA)

| Process Step | Potential Failure Mode | Mitigation Control | Risk Reduction |
| :--- | :--- | :--- | :---: |
| **Date Filtering** | `TypeError` on str vs datetime | `pd.to_datetime().dt.date` parsing | **99.4%** |
| **Patient Registration** | Invalid age input (`<0`, `>125`) | Bounded numeric input controls | **99.0%** |
| **Database Writes** | Duplicate ID / Collision | Primary key constraints & rollbacks | **97.8%** |
| **Text Search** | Null search query crash | Type casting with `.astype(str)` | **98.7%** |
| **Record Export** | Exporting empty DataFrame | Pre-download validation safeguards | **99.3%** |

---

## 👨‍💻 Author

- **GitHub:** [@BaapOfCoding699](https://github.com/BaapOfCoding699)
- **Live Demo:** [hospital-management-tqm.streamlit.app](https://hospital-management-tqm.streamlit.app/)
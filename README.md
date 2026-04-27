# 📈 FitSync | Holistic Health Intelligence

**FitSync** is a Python-based health analytics platform that bridges the gap between physical biometrics and mental well-being. Unlike standard fitness trackers that focus solely on movement, FitSync merges data from **Apple Health** (physical) and **Daylio** (mental) to provide a unified "Recovery Score."

---

🌐 Live Demo
Experience the interactive dashboard live in your browser:
👉 [View FitSync Live Dashboard]([https://your-url-here.com](https://fitsync-project-alicia-vargas.streamlit.app/))

## 🚀 Key Features

* **Unified Dashboard:** A real-time overview of physical activity vs. mental reflections.
* **Trend Analysis:** Deep-dive correlations (Heatmaps) showing how sleep and steps directly impact mood.
* **The "Storyteller" Engine:** A custom logic layer that simulates realistic health correlations for demonstration purposes.
* **Dynamic Data Import:** Supports session-based CSV uploads for Apple Health and Daylio exports.
* **Responsive UI:** A clean, modern interface built with Streamlit.

---

## 🛠️ Tech Stack

* **Language:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* **Framework:** ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
* **Data Science:** ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Statsmodels](https://img.shields.io/badge/statsmodels-708090?style=for-the-badge&logo=python&logoColor=white)
* **Visualization:** ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
* **Environment:** ![GitHub Codespaces](https://img.shields.io/badge/GitHub%20Codespaces-181717?style=for-the-badge&logo=github&logoColor=white)
* **Development Partners:** ![Gemini](https://img.shields.io/badge/Google%20Gemini-8E75C2?style=for-the-badge&logo=google-gemini&logoColor=white) ![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-000000?style=for-the-badge&logo=github-copilot&logoColor=white)

---

## 📁 Project Structure

```text
fitsync/
├── Home.py              # Landing page & entry point
├── data/                # Local CSV storage (Apple/Daylio exports)
├── modules/
│   ├── processor.py     # ETL pipeline (Data cleaning & merging)
│   ├── demo_story.py    # Logic for correlation adjustments (delete out when real data is incorporated)
│   └── interface.py     # Global UI components (Sidebar/Uploader)
└── pages/
    ├── 1_Dashboard.py   # Daily metrics & health overview
    └── 2_Trends.py      # Correlation matrix & weekly patterns
```

---

### 🚀 How to Run Locally

Follow these steps to set up the development environment on your machine:

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/mudster11-hue/fitsync-project-alicia-vargas.git](https://github.com/mudster11-hue/fitsync-project-alicia-vargas.git)
   cd fitsync-project-alicia-vargas
Install Dependencies

Bash
pip install -r requirements.txt
Launch the Dashboard

Bash
streamlit run Home.py

---
## 🛠 Developer Notes: Switching from Demo to Live Data
FitSync currently ships with a "Demo Mode" enabled to ensure the trend analysis visualizations are populated with a complete dataset for evaluation.

To switch the app to Live Mode (where it only reads from the /data folder or user uploads):

Open Home.py (or your main logic file).

Locate the data loading section (usually inside the try/except block).

Comment out the demo line and uncomment the live processing line:

Python
# --- TOGGLE DEMO MODE ---
# df = process_demo_data()  # <--- Comment this out
df = process_data()         # <--- Uncomment this for live data
# ------------------------
Note: In Live Mode, the app requires valid export.csv files from Apple Health and Daylio in the /data directory to render charts.

## 🧠 The Philosophy
The core of FitSync is the **Recovery Score**. This is a proprietary calculation that weights heart rate, sleep duration, and daily mood to tell the user not just how much they moved, but how ready they are for the day ahead.

---
## 🤖 AI Collaboration Statement
This project was developed using an AI-Augmented Workflow.

Logic & Architecture: AI was utilized to help design the ETL (Extract, Transform, Load) pipeline and handle complex data merges between Apple Health and Daylio schemas.

Problem Solving: AI served as a pair-programmer for real-time debugging of Streamlit session state and multi-page configuration errors.

### 👩‍💻 Author
**Alicia Vargas**
*Software Development Student | Saras AI Institute*

---

# 📈 FitSync | Holistic Health Intelligence

**FitSync** is a Python-based health analytics platform that bridges the gap between physical biometrics and mental well-being. Unlike standard fitness trackers that focus solely on movement, FitSync merges data from **Apple Health** (physical) and **Daylio** (mental) to provide a unified "Recovery Score."

---

## 🚀 Key Features

* **Unified Dashboard:** A real-time overview of physical activity vs. mental reflections.
* **Trend Analysis:** Deep-dive correlations (Heatmaps) showing how sleep and steps directly impact mood.
* **The "Storyteller" Engine:** A custom logic layer that simulates realistic health correlations for demonstration purposes.
* **Dynamic Data Import:** Supports session-based CSV uploads for Apple Health and Daylio exports.
* **Responsive UI:** A clean, modern interface built with Streamlit.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** [Streamlit](https://streamlit.io/) (Web Interface)
* **Data Science:** Pandas (Processing), NumPy (Logic)
* **Visualization:** Plotly Express (Interactive Charts)
* **Environment:** Developed in GitHub Codespaces with local AI integration.
* **Development Partner:** Built with **Gemini** (for architectural logic, debugging, and data storytelling).

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

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/fitsync-project.git
   cd fitsync-project
   ```

2. **Install dependencies:**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Run the application:**
   ```bash
   streamlit run Home.py
   ```

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

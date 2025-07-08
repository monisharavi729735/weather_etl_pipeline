# 🌦️ Weather ETL Pipeline with Streamlit & Airflow

A complete data pipeline project that fetches live weather data from the OpenWeatherMap API, transforms and stores it in a SQLite database, and visualizes it using a deployed Streamlit dashboard. Airflow is used locally to orchestrate the ETL process on a schedule.

---

## 🔗 Live Demo

🌐 **Hosted Streamlit Dashboard**: [Visit Website](https://weatheretlpipeline-729735.streamlit.app/)  

---

## 📸 Screenshots

### 1. 🌤️ Streamlit Dashboard
Displays current weather data for Bangalore:
![Streamlit Dashboard](https://drive.google.com/uc?export=view&id=1KOX4ovBLT1qi5sxRrk4Gl8xslecO8F8_)
![Streamlit Dashboard](https://drive.google.com/uc?export=view&id=1AL_HXD9YiVS4elb5W5_xvtSB-VRFN28q)

### 2. ⏳ Airflow DAG
Orchestrates daily ETL jobs:
![Airflow DAG flowchart](https://drive.google.com/uc?export=view&id=1lI3LjMF5V84EC6NN2mfFJ5_8_KED5IPE)
![Airflow DAG](https://drive.google.com/uc?export=view&id=1qSURtO037_IagdQ5Ucn9mL0uN9rG0kPN)

---

## 🛠️ Tech Stack

- **Python** (ETL scripts)
- **Airflow** (for scheduling ETL jobs)
- **SQLite** (lightweight local DB)
- **Streamlit** (for web dashboard)
- **Docker + Docker Compose** (for reproducible environment)
- **OpenWeatherMap API** (data source)
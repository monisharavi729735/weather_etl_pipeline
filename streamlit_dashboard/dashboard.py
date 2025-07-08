import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Weather Dashboard", layout="centered")
st.title("🌦️ Weather Dashboard")
st.write("Latest weather readings from OpenWeatherMap API (Bangalore)")

# Load from DB
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "..", "data", "weather_data.db")

print(f"Trying to connect to DB at: {db_path}")
conn = sqlite3.connect(db_path)

df = pd.read_sql("SELECT * FROM weather", conn)
conn.close()

# Show Latest
latest = df.sort_values(by="timestamp", ascending=False).iloc[0]
st.metric("Temperature", f"{latest['temperature']} °C")
st.metric("Humidity", f"{latest['humidity']}%")
st.text(f"Weather: {latest['weather']}")

# Graph
st.line_chart(df.set_index("timestamp")["temperature"])

# Raw
with st.expander("Show Raw Data"):
    st.dataframe(df.tail(10))
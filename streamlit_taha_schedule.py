import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Taha Daily Schedule", layout="wide")

DATA_FILE = "taha_schedule_data.json"

# Load existing data or create new
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        schedule_data = json.load(f)
else:
    schedule_data = {}

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_blocks = ["5-6", "6-7", "7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20", "20-21", "21-22", "22-23"]

selected_day = st.selectbox("Select Day", days)
if selected_day not in schedule_data:
    schedule_data[selected_day] = {}

st.markdown(f"### {selected_day}'s Schedule")

for idx, time_slot in enumerate(time_blocks):
    task_key = f"{selected_day}_{time_slot}"
    task_data = schedule_data[selected_day].get(time_slot, {"text": "", "check1": False, "check2": False, "note": ""})

    # Determine background color
    base_color = "#F2F2F2"  # default
    if task_data["check2"]:
        base_color = "#FFD700"  # gold for full completion
    elif task_data["check1"]:
        base_color = "#ADD8E6"  # light blue for first check

    with st.container():
        st.markdown(
            f"""
            <div style='background-color: {base_color}; padding: 10px; border-radius: 8px; margin-bottom: 10px;'>
                <strong>{time_slot}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            text = st.text_input(f"Task for {time_slot}", value=task_data["text"], key=f"text_{task_key}")
        with col2:
            check1 = st.checkbox("✔️ Start", value=task_data["check1"], key=f"check1_{task_key}")
        with col3:
            check2 = st.checkbox("✅ Done", value=task_data["check2"], key=f"check2_{task_key}")

        note = st.text_area("Note", value=str(task_data.get("note", "")), height=50, key=f"note_{task_key}")

    # Update and save only if second checkbox is checked
    task_data.update({"text": text, "check1": check1, "check2": check2, "note": note})
    schedule_data[selected_day][time_slot] = task_data

    if check2:
        with open(DATA_FILE, "w") as f:
            json.dump(schedule_data, f)

st.success("Daily Schedule Loaded. Changes save when second checkbox is ticked.")

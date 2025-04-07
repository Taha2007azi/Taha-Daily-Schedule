
import streamlit as st
import json
import os

st.set_page_config(layout="wide")
st.title("Taha's Daily Schedule")

DATA_FILE = "daily_schedule_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_slots = [
    "05:00 - 06:00", "06:00 - 07:00", "07:00 - 08:00", "08:00 - 09:00",
    "09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 13:00",
    "13:00 - 14:00", "14:00 - 15:00", "15:00 - 16:00", "16:00 - 17:00",
    "17:00 - 18:00", "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00",
    "21:00 - 22:00", "22:00 - 23:00"
]

selected_day = st.selectbox("Select Day", days)
if selected_day not in data:
    data[selected_day] = {}

st.markdown("---")

for idx, slot in enumerate(time_slots):
    task_key = f"{selected_day}_{idx}"
    if task_key not in data[selected_day]:
        data[selected_day][task_key] = {"task": "", "done_count": 0, "note": "", "archived": False}

    task_data = data[selected_day][task_key]

    col1, col2, col3 = st.columns([2, 1, 2])

    with col1:
        task = st.text_input(f"Task {slot}", value=task_data["task"], key=f"task_{task_key}")
        task_data["task"] = task

    with col2:
        done = st.checkbox("Done", value=(task_data["done_count"] > 0), key=f"done_{task_key}")
        if done:
            if task_data["done_count"] < 2:
                task_data["done_count"] += 1
        else:
            task_data["done_count"] = 0

    with col3:
        note = st.text_area("Note", value=str(task_data.get("note", "")), height=50, key=f"note_{task_key}")
        task_data["note"] = note

    # Custom style based on done_count
    bg_color = "#1E3A5F" if task_data["done_count"] == 0 else "#2C5A7B"
    if task_data["done_count"] >= 2:
        bg_color = "#4CAF50"  # Green for full done

    st.markdown(
        f"""
        <div style='background-color: {bg_color}; padding: 10px; margin-bottom: 10px; border-radius: 8px;'>
            <strong>{slot}</strong><br>
            Task: {task}<br>
            Note: {note}<br>
            Status: {"Done" if task_data["done_count"] > 0 else "Pending"}
        </div>
        """, unsafe_allow_html=True
    )

save_data(data)

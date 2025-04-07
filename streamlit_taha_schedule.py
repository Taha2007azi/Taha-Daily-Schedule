import streamlit as st
import json
import os

st.set_page_config(page_title="Taha's Daily Schedule", layout="centered")

# Path to save data
DATA_FILE = "saved_schedule.json"

# Load data from file
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        saved_data = json.load(f)
else:
    saved_data = {}

# Define colors for each day
colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

# Sample weekly schedule
weekly_schedule = {
    "Saturday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Exam Study + Lunch Breaks")
    ],
    "Sunday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Monday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 23:00", "10hr Exam Study")
    ],
    "Tuesday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Wednesday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 23:00", "10hr Exam Study")
    ],
    "Thursday": [
        ("8:00 – 8:30", "Mind Release"),
        ("8:30 – 9:00", "Workout"),
        ("9:00 – 10:30", "English"),
        ("10:30 – 23:00", "10hr Exam Study")
    ],
    "Friday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 18:00", "Coding Class"),
        ("18:00 – 21:00", "Review")
    ]
}

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: #F39C12;'>Taha's Daily Schedule</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #BDC3C7;'>Crush your goals!</h4>", unsafe_allow_html=True)

# Select day
selected_day = st.selectbox("Select Day:", list(weekly_schedule.keys()))

# Background style
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {colors[selected_day]};
            color: #ECF0F1;
            font-family: 'Tahoma', sans-serif;
        }}
        .task-complete {{
            background-color: #27ae60 !important;
            padding: 10px;
            border-radius: 8px;
        }}
        .task-block {{
            background-color: rgba(255, 255, 255, 0.07);
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader(f"Schedule for {selected_day}")

# Display tasks
for idx, (time_slot, default_task) in enumerate(weekly_schedule[selected_day]):
    task_key = f"{selected_day}_{idx}"
    task_data = saved_data.get(task_key, {"task": default_task, "done": 0, "note": ""})

    st.markdown("---")
    block_class = "task-block" if task_data["done"] < 2 else "task-complete"
    st.markdown(f"<div class='{block_class}'>", unsafe_allow_html=True)

    cols = st.columns([1, 3, 4])
    with cols[0]:
        st.markdown(f"**{time_slot}**")
    with cols[1]:
        task = st.text_input("Task", value=task_data["task"], key=f"task_{task_key}")
        done = st.checkbox("Done?", value=(task_data["done"] > 0), key=f"done_{task_key}")
    with cols[2]:
        note = st.text_area("Note", value=task_data["note"], height=50, key=f"note_{task_key}")

    # Update status
    current_done = 0
    if done:
        current_done = task_data["done"] + 1 if task_data["done"] < 2 else 2

    # Save only if done twice
    if current_done == 2:
        saved_data[task_key] = {
            "task": task,
            "done": current_done,
            "note": note
        }
        with open(DATA_FILE, "w") as f:
            json.dump(saved_data, f)

    st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
import json
import os

st.set_page_config(page_title="Weekly Plan", layout="wide")

DATA_FILE = "task_status.json"

# Load or create status file
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    saved_status_data = json.load(f)

# برنامه‌ی هفتگی
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekly_plan = {
    "Saturday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Study for Konkur"
    ],
    "Sunday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Language Class"
    ],
    "Monday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Tuesday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Language Class"
    ],
    "Wednesday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Thursday": [
        "08:00 – 08:30: Mind Clearing",
        "08:30 – 09:00: Workout",
        "09:00 – 10:30: English",
        "10:30 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Friday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 18:00: Online Programming Class",
        "18:00 – 21:00: Review the Weekly Material"
    ]
}

# استایل
st.markdown("""
    <style>
        .title {
            font-size: 2.5rem;
            color: #38b6ff;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .task-box {
            background-color: #2b2d42;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: #e0e0e0;
            font-weight: 500;
            font-size: 1.1rem;
            cursor: pointer;
        }
        .task-done {
            background-color: #007f5f !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Your Weekly Plan</div>', unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)

tasks = weekly_plan[selected_day]

# مقداردهی اولیه
if selected_day not in saved_status_data:
    saved_status_data[selected_day] = [False] * len(tasks)

# کپی برای تغییرات موقت
if "temp_status" not in st.session_state:
    st.session_state.temp_status = {}

if selected_day not in st.session_state.temp_status:
    st.session_state.temp_status[selected_day] = saved_status_data[selected_day][:]

# نمایش تسک‌ها
for i, task in enumerate(tasks):
    task_key = f"{selected_day}_{i}"
    if st.session_state.temp_status[selected_day][i]:
        st.markdown(f'<div class="task-box task-done">{task}</div>', unsafe_allow_html=True)
    else:
        if st.button(task, key=task_key):
            st.session_state.temp_status[selected_day][i] = True
            st.rerun()
        else:
            st.markdown(f'<div class="task-box">{task}</div>', unsafe_allow_html=True)

# دکمه‌های Apply و Reset
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Apply"):
        saved_status_data[selected_day] = st.session_state.temp_status[selected_day][:]
        with open(DATA_FILE, "w") as f:
            json.dump(saved_status_data, f)
        st.success("Changes applied and saved!")
with col2:
    if st.button("❌ Reset"):
        st.session_state.temp_status[selected_day] = [False] * len(tasks)
        st.rerun()

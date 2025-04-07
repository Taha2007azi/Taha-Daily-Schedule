import streamlit as st
import json
import os

st.set_page_config(page_title="Weekly Step Planner", layout="wide")

DATA_FILE = "planner_state.json"

# ذخیره و بارگذاری دیتا
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# استایل‌ها
st.markdown("""
    <style>
        .title { font-size: 2.5rem; color: #38b6ff; font-weight: bold; text-align: center; margin-bottom: 2rem; }
        .task-box { background-color: #2b2d42; padding: 1rem; border-radius: 12px; margin-bottom: 1rem; color: #e0e0e0; font-weight: 500; font-size: 1.2rem; }
        .task-done { background-color: #007f5f; padding: 1rem; border-radius: 12px; margin-bottom: 1rem; color: white; font-weight: 500; font-size: 1.2rem; }
        .motiv { background: linear-gradient(to right, #38b6ff, #00b4d8); padding: 0.8rem; border-radius: 10px; color: white; text-align: center; font-size: 1.1rem; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# پیام انگیزشی و عنوان
st.markdown('<div class="motiv">Every step counts, Taha. Let’s make this week powerful!</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Your Weekly Step Planner</div>', unsafe_allow_html=True)

# دیتا اولیه
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekly_plan = {
    "Saturday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
    "Sunday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
    "Monday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
    "Tuesday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
    "Wednesday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
    "Thursday": ["08:00 – 08:30: Mind Clearing", "08:30 – 09:00: Workout", "09:00 – 10:30: English"],
    "Friday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout", "06:00 – 07:30: English"],
}

data = load_data()

selected_day = st.selectbox("Choose a day:", days)
if selected_day not in data:
    data[selected_day] = {"tasks": [False] * len(weekly_plan[selected_day])}

# نمایش تسک‌ها
st.markdown(f"### {selected_day}")
for i, task in enumerate(weekly_plan[selected_day]):
    done = st.checkbox(task, value=data[selected_day]["tasks"][i], key=f"{selected_day}_{i}")
    data[selected_day]["tasks"][i] = done
    if done:
        st.markdown(f'<div class="task-done">{task}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="task-box">{task}</div>', unsafe_allow_html=True)

# دکمه‌ها
col1, col2 = st.columns(2)
with col1:
    if st.button("Reset All"):
        data[selected_day]["tasks"] = [False] * len(weekly_plan[selected_day])
        save_data(data)
        st.rerun()
with col2:
    if st.button("Apply Changes"):
        save_data(data)
        st.success("Changes saved!")


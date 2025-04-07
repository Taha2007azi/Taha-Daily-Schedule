import streamlit as st
import json
import os

st.set_page_config(page_title="Weekly Plan", layout="wide")

DATA_FILE = "task_status.json"
TEXT_FILE = "task_texts.json"

# فایل‌های اولیه
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)
if not os.path.exists(TEXT_FILE):
    with open(TEXT_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    saved_status_data = json.load(f)
with open(TEXT_FILE, "r") as f:
    saved_text_data = json.load(f)

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
            margin-bottom: 0.5rem;
            color: #e0e0e0;
            font-weight: 500;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        .task-done {
            background-color: #007f5f !important;
            color: white !important;
        }
        .btn-style button {
            width: 100%;
            font-weight: bold;
            font-size: 1.1rem;
            height: 3rem;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Your Weekly Plan</div>', unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)
tasks = weekly_plan[selected_day]

# مقداردهی اولیه
if selected_day not in saved_status_data:
    saved_status_data[selected_day] = [False] * len(tasks)
if selected_day not in saved_text_data:
    saved_text_data[selected_day] = tasks[:]

if "temp_status" not in st.session_state:
    st.session_state.temp_status = {}
if "temp_texts" not in st.session_state:
    st.session_state.temp_texts = {}

if selected_day not in st.session_state.temp_status:
    st.session_state.temp_status[selected_day] = saved_status_data[selected_day][:]
if selected_day not in st.session_state.temp_texts:
    st.session_state.temp_texts[selected_day] = saved_text_data[selected_day][:]

# نمایش تسک‌ها
for i in range(len(tasks)):
    task_key = f"{selected_day}_{i}"
    text = st.session_state.temp_texts[selected_day][i]
    
    # نمایش با استایل مناسب
    box_class = "task-box"
    if st.session_state.temp_status[selected_day][i]:
        box_class += " task-done"
    
    # کلیک روی متن برای تغییر وضعیت
    if st.button(text, key=f"btn_{task_key}"):
        st.session_state.temp_status[selected_day][i] = not st.session_state.temp_status[selected_day][i]
        st.rerun()

    # باکس تغییر متن
    new_text = st.text_input("Edit:", value=text, key=f"text_{task_key}")
    st.session_state.temp_texts[selected_day][i] = new_text

# دکمه‌ها
col1, col2 = st.columns(2)
with col1:
    with st.container():
        st.markdown('<div class="btn-style">', unsafe_allow_html=True)
        if st.button("✅ Apply"):
            saved_status_data[selected_day] = st.session_state.temp_status[selected_day][:]
            saved_text_data[selected_day] = st.session_state.temp_texts[selected_day][:]
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            with open(TEXT_FILE, "w") as f:
                json.dump(saved_text_data, f)
            st.success("Changes saved successfully!")
        st.markdown('</div>', unsafe_allow_html=True)
with col2:
    with st.container():
        st.markdown('<div class="btn-style">', unsafe_allow_html=True)
        if st.button("❌ Reset"):
            st.session_state.temp_status[selected_day] = [False] * len(tasks)
            st.session_state.temp_texts[selected_day] = tasks[:]
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

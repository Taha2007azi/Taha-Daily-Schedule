import streamlit as st
st.set_page_config(page_title="Taha's Planner", layout="wide")

import datetime

st.markdown(
    """
    <style>
        body {
            background-color: #1c1e26;
        }
        .task {
            background-color: #2b2d3a;
            border-radius: 15px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .done {
            background-color: #007f5f;
            color: white;
        }
        .title {
            font-size: 2rem;
            color: #38b6ff;
            font-weight: bold;
        }
        .motiv {
            background: linear-gradient(to right, #38b6ff, #00b4d8);
            padding: 0.8rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 1.1rem;
        }
    </style>
    """, unsafe_allow_html=True
)

# پیام انگیزشی بالا
st.markdown('<div class="motiv">Keep showing up, no matter what. Greatness takes consistency, not luck.</div>', unsafe_allow_html=True)

st.markdown('<div class="title">Your Weekly Planner</div>', unsafe_allow_html=True)

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# دیتای برنامه - می‌تونه بعداً از فایل یا دیتابیس خونده شه
weekly_plan = {
    "Saturday": ["Morning Routine", "Study Math", "Review Language"],
    "Sunday": ["Morning Routine", "Study Physics", "Practice English"],
    "Monday": ["Morning Routine", "School", "Language Class"],
    "Tuesday": ["Morning Routine", "Study Algorithms", "Deep Work"],
    "Wednesday": ["Morning Routine", "School", "Review"],
    "Thursday": ["Morning Routine", "Mock Exam", "Project Work"],
    "Friday": ["Morning Routine", "Programming Class", "Relax"]
}

# ساخت هر روز با تسک‌ها
for day in days:
    st.subheader(day)
    for i, task in enumerate(weekly_plan[day]):
        col1, col2 = st.columns([1, 5])
        with col1:
            check1 = st.checkbox(f"{day}_{i}_check1", label_visibility="collapsed")
        with col2:
            if check1:
                check2 = st.checkbox(f"{day}_{i}_check2", label=task)
                if check2:
                    st.markdown(f'<div class="task done">{task} - Done!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="task">{task}</div>', unsafe_allow_html=True)
    st.markdown("---")

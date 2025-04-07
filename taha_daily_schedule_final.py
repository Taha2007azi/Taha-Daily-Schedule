import streamlit as st

# باید اولین خط باشه
st.set_page_config(page_title="Taha's Planner", layout="wide")

# استایل باکلاس و رنگ‌های سرد
st.markdown(
    """
    <style>
        body {
            background-color: #1e1e2f;
        }
        .task {
            background-color: #2b2d42;
            border-radius: 12px;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            color: #e0e0e0;
            font-weight: 500;
        }
        .done {
            background-color: #007f5f;
            color: white;
        }
        .title {
            font-size: 2.2rem;
            color: #38b6ff;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .motiv {
            background: linear-gradient(to right, #38b6ff, #00b4d8);
            padding: 0.8rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        .day-header {
            font-size: 1.4rem;
            color: #5fdde5;
            margin-top: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True
)

# پیام انگیزشی بالا
st.markdown('<div class="motiv">Every day you show up is one step closer to greatness. Let’s crush this week, Taha!</div>', unsafe_allow_html=True)

# تیتر صفحه
st.markdown('<div class="title">Your Full Weekly Planner</div>', unsafe_allow_html=True)

# روزها
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# برنامه دقیق هفتگی با تایم‌بندی روتین‌ها و تسک‌ها
weekly_plan = {
    "Saturday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Konkur Study"
    ],
    "Sunday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Language Class"
    ],
    "Monday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Tuesday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:00: Rest",
        "16:00 – 23:00: Language Class"
    ],
    "Wednesday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Thursday": [
        "08:00 – 08:30: Mental Clearing",
        "08:30 – 09:00: Exercise",
        "09:00 – 10:30: English",
        "10:30 – 23:00: Heavy Konkur Study (~10h)"
    ],
    "Friday": [
        "05:00 – 05:30: Mental Clearing",
        "05:30 – 06:00: Exercise",
        "06:00 – 07:30: English",
        "08:00 – 18:00: Online Programming Class",
        "18:00 – 21:00: Review the Weekly Material"
    ]
}

# رندر کل هفته
for day in days:
    st.markdown(f'<div class="day-header">{day}</div>', unsafe_allow_html=True)
    for i, task in enumerate(weekly_plan[day]):
        task_key = f"{day}_{i}_done"
        done = st.checkbox(label=task, key=task_key)
        if done:
            st.markdown(f'<div class="task done">{task} - Done!</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="task">{task}</div>', unsafe_allow_html=True)

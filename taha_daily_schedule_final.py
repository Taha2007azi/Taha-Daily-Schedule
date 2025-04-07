import streamlit as st

st.set_page_config(page_title="Weekly Step Planner", layout="wide")

# استایل کلی
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
        }
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
            font-size: 1.2rem;
        }
        .task-done {
            background-color: #007f5f;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: white;
            font-weight: 500;
            font-size: 1.2rem;
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
        .custom-textarea {
            font-family: 'Courier New', monospace;
            font-size: 1.1rem;
            background-color: #f2f2f2;
            border-radius: 10px;
            padding: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# پیام انگیزشی
st.markdown('<div class="motiv">Every step counts, Taha. Let’s make this week powerful!</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Your Weekly Step Planner</div>', unsafe_allow_html=True)

# روزها و برنامه
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

selected_day = st.selectbox("Choose a day:", days)

if f"{selected_day}_index" not in st.session_state:
    st.session_state[f"{selected_day}_index"] = 0

st.markdown(f"### {selected_day}")

tasks = weekly_plan[selected_day]
index = st.session_state[f"{selected_day}_index"]

for i, task in enumerate(tasks):
    if i < index:
        st.markdown(f'<div class="task-done">{task} - Done!</div>', unsafe_allow_html=True)
    elif i == index:
        st.markdown(f'<div class="task-box">{task}</div>', unsafe_allow_html=True)
        if st.checkbox("Mark as done", key=f"{selected_day}_{i}"):
            st.session_state[f"{selected_day}_index"] += 1
            st.rerun()
        break

if index >= len(tasks):
    st.success(f"All tasks for {selected_day} completed!")

    score = st.slider("Rate your performance today (1–5)", 1, 5, 3, key=f"{selected_day}_score")
    st.markdown("### Daily Reflection:")
    report = st.text_area("Your Notes", placeholder="Write your thoughts about today...", height=200, key=f"{selected_day}_report")

    if report:
        st.markdown(f"<div class='custom-textarea'>{report}</div>", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(page_title="Saturday Planner", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
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
        .title {
            font-size: 2.5rem;
            color: #38b6ff;
            font-weight: bold;
            text-align: center;
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

st.markdown('<div class="title">Saturday Plan</div>', unsafe_allow_html=True)

tasks = [
    "05:00 – 05:30: Mind Clearing",
    "05:30 – 06:00: Workout",
    "06:00 – 07:30: English",
    "08:00 – 15:00: School",
    "15:00 – 16:00: Rest",
    "16:00 – 23:00: Study for Konkur"
]

if 'saturday_task_index' not in st.session_state:
    st.session_state.saturday_task_index = 0

current_index = st.session_state.saturday_task_index

if current_index < len(tasks):
    current_task = tasks[current_index]
    st.markdown(f'<div class="task-box">{current_task}</div>', unsafe_allow_html=True)
    task_done = st.checkbox("Done", key=f"task_{current_index}")

    if task_done and st.button("Next"):
        st.session_state.saturday_task_index += 1
        st.rerun()  # استفاده رسمی‌تر از rerun
else:
    st.success("You’ve completed all tasks for Saturday!")

    score = st.slider("Rate your performance today (1-5)", 1, 5, 3)

    st.markdown("### Write your daily reflection:")
    report = st.text_area("Your Notes", placeholder="Write something about your day...", height=200, key="saturday_report")

    if report:
        st.markdown(f"<div class='custom-textarea'>{report}</div>", unsafe_allow_html=True)

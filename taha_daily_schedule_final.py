import streamlit as st

# ---------- Settings ----------
st.set_page_config(page_title="Taha's Daily Planner", layout="wide")

# ---------- Styling ----------
st.markdown("""
    <style>
        body { background-color: #0f172a; color: white; }
        .title { font-size: 32px; font-weight: bold; color: #22d3ee; margin-bottom: 20px; }
        .motivation { font-size: 20px; color: #4ade80; margin-bottom: 30px; }
        .task-box { background-color: #1e293b; padding: 10px; border-radius: 12px; margin-bottom: 10px; }
        .task-box.done { background-color: #14532d; }
    </style>
""", unsafe_allow_html=True)

# ---------- Motivation Text ----------
st.markdown('<div class="title">Taha\'s Powerful Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="motivation">Level up every day. No excuses. Just pure growth.</div>', unsafe_allow_html=True)

# ---------- Weekly Schedule ----------
week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
tasks_per_day = {
    'Saturday': [("08:00 - Morning Routine", False), ("10:00 - Study Math", False)],
    'Sunday': [("08:00 - Language Class", False), ("11:00 - Review Notes", False)],
    'Monday': [("08:00 - Gym", False), ("09:30 - Study Physics", False)],
    'Tuesday': [("08:00 - Practice English", False), ("10:30 - Programming Project", False)],
    'Wednesday': [("08:00 - Mock Test", False), ("11:00 - Analyze Mistakes", False)],
    'Thursday': [("08:00 - Focus Study", False), ("13:00 - Deep Work", False)],
    'Friday': [("09:00 - Review Week", False), ("14:00 - Relax & Read", False)]
}

# ---------- Select Day ----------
selected_day = st.selectbox("Choose a day", week_days)

# ---------- Show Tasks ----------
st.subheader(f"Plan for {selected_day}")
day_tasks = tasks_per_day[selected_day]

for idx, (task_text, _) in enumerate(day_tasks):
    task_key_1 = f"{selected_day}_{idx}_check1"
    task_key_2 = f"{selected_day}_{idx}_check2"

    if not st.session_state.get(task_key_1, False):
        with st.container():
            st.markdown(f'<div class="task-box">{task_text}</div>', unsafe_allow_html=True)
            if st.checkbox("Start", key=task_key_1):
                st.experimental_rerun()

    elif not st.session_state.get(task_key_2, False):
        with st.container():
            st.markdown(f'<div class="task-box">{task_text}</div>', unsafe_allow_html=True)
            if st.checkbox("Done", key=task_key_2):
                st.experimental_rerun()

# ---------- Done Tasks Automatically Hidden ----------
# Future versions will support showing Done list or restore buttons

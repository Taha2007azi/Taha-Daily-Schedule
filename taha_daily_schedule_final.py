import streamlit as st

st.set_page_config(page_title="Taha's Planner", layout="wide")  # باید اولین دستور باشه

# ---------- Style ----------
st.markdown("""
    <style>
        body { background-color: #0f172a; color: white; }
        .title { font-size: 32px; font-weight: bold; color: #22d3ee; margin-bottom: 20px; }
        .motivation { font-size: 20px; color: #4ade80; margin-bottom: 30px; }
        .task-box { background-color: #1e293b; padding: 10px; border-radius: 12px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ---------- Motivation Text ----------
st.markdown('<div class="title">Taha\'s Powerful Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="motivation">Level up every day. No excuses. Just pure growth.</div>', unsafe_allow_html=True)

# ---------- Week and Tasks ----------
week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
default_tasks = {
    'Saturday': ["08:00 - Morning Routine", "10:00 - Study Math"],
    'Sunday': ["08:00 - Language Class", "11:00 - Review Notes"],
    'Monday': ["08:00 - Gym", "09:30 - Study Physics"],
    'Tuesday': ["08:00 - Practice English", "10:30 - Programming Project"],
    'Wednesday': ["08:00 - Mock Test", "11:00 - Analyze Mistakes"],
    'Thursday': ["08:00 - Focus Study", "13:00 - Deep Work"],
    'Friday': ["09:00 - Review Week", "14:00 - Relax & Read"]
}

# ---------- Initialize session state ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = {day: list(default_tasks[day]) for day in week_days}
if "started" not in st.session_state:
    st.session_state.started = {day: [False]*len(default_tasks[day]) for day in week_days}
if "done" not in st.session_state:
    st.session_state.done = {day: [False]*len(default_tasks[day]) for day in week_days}

# ---------- Select Day ----------
selected_day = st.selectbox("Choose a day", week_days)

# ---------- Show Tasks ----------
st.subheader(f"Plan for {selected_day}")
for idx, task in enumerate(st.session_state.tasks[selected_day]):
    if st.session_state.done[selected_day][idx]:
        continue  # skip done tasks

    box_class = "task-box"
    with st.container():
        st.markdown(f'<div class="{box_class}">{task}</div>', unsafe_allow_html=True)

        if not st.session_state.started[selected_day][idx]:
            if st.checkbox("Start", key=f"{selected_day}_{idx}_start"):
                st.session_state.started[selected_day][idx] = True
                st.rerun()
            break  # show one task at a time

        elif not st.session_state.done[selected_day][idx]:
            if st.checkbox("Done", key=f"{selected_day}_{idx}_done"):
                st.session_state.done[selected_day][idx] = True
                st.rerun()
            break  # show one task at a time
import streamlit as st

st.set_page_config(page_title="Taha's Planner", layout="wide")

# ---------- Style ----------
st.markdown("""
    <style>
        body { background-color: #0f172a; color: white; }
        .title { font-size: 32px; font-weight: bold; color: #22d3ee; margin-bottom: 20px; }
        .motivation { font-size: 20px; color: #4ade80; margin-bottom: 30px; }
        .task-box { background-color: #1e293b; padding: 10px; border-radius: 12px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# ---------- Motivation Text ----------
st.markdown('<div class="title">Taha\'s Powerful Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="motivation">Level up every day. No excuses. Just pure growth.</div>', unsafe_allow_html=True)

# ---------- Week and Tasks ----------
week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
default_tasks = {
    'Saturday': ["08:00 - Morning Routine", "10:00 - Study Math"],
    'Sunday': ["08:00 - Language Class", "11:00 - Review Notes"],
    'Monday': ["08:00 - Gym", "09:30 - Study Physics"],
    'Tuesday': ["08:00 - Practice English", "10:30 - Programming Project"],
    'Wednesday': ["08:00 - Mock Test", "11:00 - Analyze Mistakes"],
    'Thursday': ["08:00 - Focus Study", "13:00 - Deep Work"],
    'Friday': ["09:00 - Review Week", "14:00 - Relax & Read"]
}

# ---------- Initialize session state ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = {day: list(default_tasks[day]) for day in week_days}
if "started" not in st.session_state:
    st.session_state.started = {day: [False]*len(default_tasks[day]) for day in week_days}
if "done" not in st.session_state:
    st.session_state.done = {day: [False]*len(default_tasks[day]) for day in week_days}

# ---------- Select Day ----------
selected_day = st.selectbox("Choose a day", week_days)

# ---------- Show Tasks ----------
st.subheader(f"Plan for {selected_day}")
for idx, task in enumerate(st.session_state.tasks[selected_day]):
    if st.session_state.done[selected_day][idx]:
        continue  # skip done tasks

    box_class = "task-box"
    with st.container():
        st.markdown(f'<div class="{box_class}">{task}</div>', unsafe_allow_html=True)

        if not st.session_state.started[selected_day][idx]:
            if st.checkbox("Start", key=f"{selected_day}_{idx}_start"):
                st.session_state.started[selected_day][idx] = True
                st.rerun()
            break  # show one task at a time

        elif not st.session_state.done[selected_day][idx]:
            if st.checkbox("Done", key=f"{selected_day}_{idx}_done"):
                st.session_state.done[selected_day][idx] = True
                st.rerun()
            break  # show one task at a time

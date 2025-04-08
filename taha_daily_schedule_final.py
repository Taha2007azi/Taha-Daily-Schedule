import streamlit as st
import json
import os

# ---------- Login System ----------
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "taha2007azi" and password == "_20TaHa07_":
            st.session_state.logged_in = True
        else:
            st.error("Incorrect username or password.")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()
# ---------- End Login System ----------

st.set_page_config(page_title="Weekly Plan", layout="wide")

motivational_text = "“Push yourself, because no one else is going to do it for you.”"
st.markdown(f"""
    <div style='
        text-align: center;
        font-size: 1.8rem;
        font-weight: bold;
        color: #4dd0e1;
        margin: 2rem 0;
        padding: 1rem;
        background-color: #1e1e1e;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
    '>
        {motivational_text}
    </div>
""", unsafe_allow_html=True)

DATA_FILE = "task_status.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    saved_status_data = json.load(f)

days = ["Nothing", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
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
            transition: all 0.3s ease;
        }
        .task-box:hover {
            background-color: #3d3f5c;
        }
        .task-done {
            background-color: #009688 !important;
            color: white !important;
        }
        button.task-button {
            background: none;
            border: none;
            width: 100%;
            text-align: left;
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Your Weekly Plan</div>', unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)

if selected_day != "Nothing":
    tasks = weekly_plan[selected_day]

    if selected_day not in saved_status_data:
        saved_status_data[selected_day] = [False] * len(tasks)

    if "temp_status" not in st.session_state:
        st.session_state.temp_status = {}
    if selected_day not in st.session_state.temp_status:
        st.session_state.temp_status[selected_day] = saved_status_data[selected_day][:]

    for i, task in enumerate(tasks):
        key = f"{selected_day}_{i}"
        if st.session_state.temp_status[selected_day][i]:
            st.markdown(f'<div class="task-box task-done">{task}</div>', unsafe_allow_html=True)
        else:
            if st.button(f"{task}", key=key):
                st.session_state.temp_status[selected_day][i] = True
                st.rerun()

    st.markdown("### Notes")
    note_key = f"{selected_day}_note"
    default_note = saved_status_data.get(note_key, "")
    note_text = st.text_area("Write your daily report or notes here:", value=default_note, key=f"note_{selected_day}", height=150)

    with st.form(key="action_form"):
        col1, col2 = st.columns(2)
        with col1:
            apply_click = st.form_submit_button(label="✅ Apply")
        with col2:
            reset_click = st.form_submit_button(label="❌ Reset")

        if apply_click:
            saved_status_data[selected_day] = st.session_state.temp_status[selected_day][:]
            saved_status_data[note_key] = note_text
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.success("Changes and note saved!")

        if reset_click:
            st.session_state.temp_status[selected_day] = [False] * len(tasks)
            saved_status_data[selected_day] = [False] * len(tasks)
            saved_status_data[note_key] = ""
            if f"note_{selected_day}" in st.session_state:
                del st.session_state[f"note_{selected_day}"]
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.success(f"{selected_day} has been reset successfully!")
            st.rerun()
else:
    st.markdown("### No tasks today. Enjoy your time or take a break!")

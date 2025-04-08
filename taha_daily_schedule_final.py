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

# ---------- Style ----------
st.markdown("""
    <style>
        .task {
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 10px;
            background-color: #2b2d42;
            color: white;
            font-size: 1.1rem;
            font-weight: 500;
            transition: background-color 0.3s ease;
            cursor: pointer;
        }
        .task.done {
            background-color: #28a745 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#4dd0e1;'>Your Weekly Plan</h1>", unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)

if selected_day != "Nothing":
    tasks = weekly_plan[selected_day]

    if selected_day not in saved_status_data:
        saved_status_data[selected_day] = [False] * len(tasks)

    if "task_status" not in st.session_state:
        st.session_state.task_status = saved_status_data

    for i, task in enumerate(tasks):
        status = st.session_state.task_status[selected_day][i]
        class_name = "task done" if status else "task"
        if st.markdown(f"<div class='{class_name}' onClick='window.location.href=\"?task={i}\"'>{task}</div>", unsafe_allow_html=True):
            pass

    query_params = st.query_params
    if "task" in query_params:
        task_id = int(query_params["task"][0])
        st.session_state.task_status[selected_day][task_id] = not st.session_state.task_status[selected_day][task_id]
        saved_status_data[selected_day] = st.session_state.task_status[selected_day]
        with open(DATA_FILE, "w") as f:
            json.dump(saved_status_data, f)
        st.experimental_rerun()

    note_key = f"{selected_day}_note"
    note = st.text_area("Write notes for the day:", value=saved_status_data.get(note_key, ""), height=150)
    
    if st.button("Save Note"):
        saved_status_data[note_key] = note
        with open(DATA_FILE, "w") as f:
            json.dump(saved_status_data, f)
        st.success("Note saved!")

else:
    st.info("No tasks today. Enjoy your free time!")


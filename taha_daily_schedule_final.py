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

# ---------- Weekly Plan ----------
days = ["Nothing", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekly_plan = {
    "Saturday": ["05:00 – 05:30: Mind Clearing", "05:30 – 06:00: Workout"],
    "Sunday": ["06:00 – 07:30: English", "08:00 – 15:00: School"],
}

st.markdown("""
    <style>
        .task-box {
            padding: 0.75rem 1rem;
            border-radius: 8px;
            margin-bottom: 0.5rem;
            background-color: #2b2d42;
            color: #e0e0e0;
            font-weight: 500;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        .task-box.done {
            background-color: #00a676 !important;
            color: white !important;
        }
        .clickable {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)

if selected_day != "Nothing":
    tasks = weekly_plan[selected_day]

    if "task_status" not in st.session_state:
        st.session_state.task_status = {}

    if selected_day not in st.session_state.task_status:
        st.session_state.task_status[selected_day] = saved_status_data.get(selected_day, [False]*len(tasks))

    for i, task in enumerate(tasks):
        task_key = f"{selected_day}_{i}"

        status = st.session_state.task_status[selected_day][i]
        div_class = "task-box clickable done" if status else "task-box clickable"

        if st.markdown(f"""
            <div class="{div_class}" onclick="fetch('/?toggle={task_key}').then(() => window.location.reload())">
                {task}
            </div>
        """, unsafe_allow_html=True):
            pass

    # Update query params manually
    query_params = st.query_params
    if "toggle" in query_params:
        task_key = query_params["toggle"][0]
        day, idx = task_key.split("_")
        idx = int(idx)
        st.session_state.task_status[day][idx] = not st.session_state.task_status[day][idx]

        # Save
        saved_status_data[day] = st.session_state.task_status[day]
        with open(DATA_FILE, "w") as f:
            json.dump(saved_status_data, f)
        st.query_params.clear()
        st.rerun()

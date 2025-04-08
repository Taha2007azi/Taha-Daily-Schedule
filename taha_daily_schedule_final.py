import streamlit as st
import json
import os

# ---------- Login ----------
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

# ---------- Config ----------
st.set_page_config(page_title="Taha's Plan", layout="wide")
DATA_FILE = "task_status.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    saved_status_data = json.load(f)

# ---------- Plan ----------
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
        "15:00 – 16:30: Rest",
        "16:30 – 23:00: Language Class + Rest"
    ],
    "Monday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "Study: 08:00 – 18:00 (10hr plan)"
    ],
    "Tuesday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "08:00 – 15:00: School",
        "15:00 – 16:30: Rest",
        "16:30 – 23:00: Language Class + Rest"
    ],
    "Wednesday": [
        "05:00 – 05:30: Mind Clearing",
        "05:30 – 06:00: Workout",
        "06:00 – 07:30: English",
        "Study: 08:00 – 18:00 (10hr plan)"
    ],
    "Thursday": [
        "08:00 – 08:30: Mind Clearing",
        "08:30 – 09:00: Workout",
        "09:00 – 10:30: English",
        "Study: 10:30 – 21:30 (10hr plan)"
    ],
    "Friday": [
        "08:00 – 08:30: Mind Clearing",
        "08:30 – 09:00: Workout",
        "09:00 – 10:30: English",
        "10:30 – 18:00: Programming Class"
    ],
}

# ---------- CSS ----------
st.markdown("""
    <style>
    div.stButton > button {
        background: none;
        border: none;
        padding: 10px 0;
        color: white;
        font-size: 1.1rem;
        text-align: left;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #444444;
    }
    .completed > button {
        background-color: #2ecc71 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- UI ----------
selected_day = st.selectbox("Select a day:", days)

if selected_day != "Nothing":
    tasks = weekly_plan[selected_day]

    if selected_day not in saved_status_data:
        saved_status_data[selected_day] = [False] * len(tasks)

    if "task_status" not in st.session_state:
        st.session_state.task_status = saved_status_data

    st.subheader(f"Plan for {selected_day}")

    for i, task in enumerate(tasks):
        task_key = f"{selected_day}_{i}"
        status = st.session_state.task_status[selected_day][i]

        container = st.container()
        with container:
            if status:
                with st.container():
                    st.markdown(f"""
                        <div class="completed">
                            <button disabled>{task}</button>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                if st.button(task, key=task_key):
                    st.session_state.task_status[selected_day][i] = True
                    saved_status_data[selected_day][i] = True
                    with open(DATA_FILE, "w") as f:
                        json.dump(saved_status_data, f)

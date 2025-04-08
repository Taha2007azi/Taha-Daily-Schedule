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
        .task {
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            border-radius: 8px;
            background-color: #2c2f4a;
            color: #e0e0e0;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .task.done {
            background-color: #28a745 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Your Weekly Plan</div>', unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", days)

if selected_day != "Nothing":
    tasks = weekly_plan[selected_day]

    if selected_day not in saved_status_data:
        saved_status_data[selected_day] = [False] * len(tasks)

    if "clicked" not in st.session_state:
        st.session_state.clicked = {}
    if selected_day not in st.session_state.clicked:
        st.session_state.clicked[selected_day] = saved_status_data[selected_day][:]

    for i, task in enumerate(tasks):
        task_class = "task done" if st.session_state.clicked[selected_day][i] else "task"
        task_html = f"<div class='{task_class}' onclick=\"window.location.href='/?clicked={selected_day}_{i}'\">{task}</div>"
        st.markdown(task_html, unsafe_allow_html=True)

    query_params = st.experimental_get_query_params()
    if "clicked" in query_params:
        clicked_val = query_params["clicked"][0]
        day_key, idx_str = clicked_val.split("_")
        idx = int(idx_str)
        if day_key in st.session_state.clicked:
            st.session_state.clicked[day_key][idx] = not st.session_state.clicked[day_key][idx]
        st.experimental_set_query_params()  # clear after processing

    with st.form(key="actions"):
        col1, col2 = st.columns(2)
        if col1.form_submit_button("✅ Apply"):
            saved_status_data[selected_day] = st.session_state.clicked[selected_day][:]
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.success("Changes saved!")

        if col2.form_submit_button("❌ Reset"):
            st.session_state.clicked[selected_day] = [False] * len(tasks)
            saved_status_data[selected_day] = [False] * len(tasks)
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.rerun()
else:
    st.markdown("### No tasks today. Enjoy your time or take a break!")

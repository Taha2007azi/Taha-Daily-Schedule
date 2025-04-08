# Taha's Final Daily Schedule App
import streamlit as st
import json
import os
from datetime import datetime

# -------------------- Config --------------------
st.set_page_config(page_title="Taha's Daily Schedule", layout="wide")
st.markdown("""
    <style>
        .done-task {
            background-color: #203040;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 5px;
        }
        .task-block {
            background-color: #1c1f26;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .check-btns button {
            margin-right: 10px;
            backdrop-filter: blur(5px);
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- User Login --------------------
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "taha2007azi" and password == "_20TaHa07_":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong credentials")

if "logged_in" not in st.session_state:
    login()
    st.stop()

# -------------------- Save/Load --------------------
SAVE_FILE = "saved_state.json"
def load_state():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_state():
    with open(SAVE_FILE, "w") as f:
        json.dump(st.session_state.to_dict(), f)

state_data = load_state()
for key, val in state_data.items():
    st.session_state[key] = val

# -------------------- Daily Plan --------------------
daily_schedule = {
    "Saturday": ["Wake up & Routine", "School", "Study Time"],
    "Sunday": ["Wake up & Routine", "School", "Language Class"],
    "Monday": ["Wake up & Routine", "Heavy Study"],
    "Tuesday": ["Wake up & Routine", "School", "Language Class"],
    "Wednesday": ["Wake up & Routine", "Heavy Study"],
    "Thursday": ["Wake up Late", "Heavy Study"],
    "Friday": ["Wake up & Routine", "Programming Class"]
}

# -------------------- Functions --------------------
def render_day(day, tasks):
    st.subheader(day)
    for task in tasks:
        key1 = f"{day}_{task}_check1"
        key2 = f"{day}_{task}_check2"
        note_key = f"{day}_{task}_note"

        if key1 not in st.session_state:
            st.session_state[key1] = False
        if key2 not in st.session_state:
            st.session_state[key2] = False
        if note_key not in st.session_state:
            st.session_state[note_key] = ""

        with st.container():
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                st.markdown(f"### {task}")
                if not st.session_state[key1]:
                    if st.checkbox("Check 1", key=key1):
                        st.rerun()
                elif not st.session_state[key2]:
                    if st.checkbox("Check 2", key=key2):
                        st.success("Done!")
                        st.rerun()
                else:
                    st.markdown(
                        f"<div class='done-task'><b>{task}</b> - Completed</div>", unsafe_allow_html=True)
            with col2:
                st.text_area("Note", key=note_key, height=100)

# -------------------- UI Layout --------------------
st.title("Taha's Full Daily Schedule")
day = st.selectbox("Choose a day", list(daily_schedule.keys()))
render_day(day, daily_schedule[day])

colA, colB, colC = st.columns(3)
with colA:
    if st.button("Apply"):
        save_state()
        st.success("Saved!")
with colB:
    if st.button("Reset"):
        for task in daily_schedule[day]:
            st.session_state[f"{day}_{task}_check1"] = False
            st.session_state[f"{day}_{task}_check2"] = False
            st.session_state[f"{day}_{task}_note"] = ""
        save_state()
        st.rerun()
with colC:
    if st.button("Reset ALL"):
        for d, tasks in daily_schedule.items():
            for task in tasks:
                st.session_state[f"{d}_{task}_check1"] = False
                st.session_state[f"{d}_{task}_check2"] = False
                st.session_state[f"{d}_{task}_note"] = ""
        save_state()
        st.rerun()

# -------------------- END --------------------

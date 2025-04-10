import streamlit as st
import json
import os
from datetime import datetime

# File paths
PLAN_FILE = "weekly_plan.json"
STATUS_FILE = "task_status.json"

# Default plan if no file exists
default_plan = {
    "Saturday": ["Study Math", "Study Physics"],
    "Sunday": ["Study Chemistry", "Revise Math"],
    "Monday": ["Biology Homework", "Watch Physics Lecture"],
    "Tuesday": ["Review Notes", "Practice Problems"],
    "Wednesday": ["Group Study", "Online Quiz"],
    "Thursday": ["Rest", "Plan Next Week"],
    "Friday": ["Programming Class"]
}

# Load or initialize weekly plan
if not os.path.exists(PLAN_FILE):
    with open(PLAN_FILE, "w") as f:
        json.dump(default_plan, f)

with open(PLAN_FILE, "r") as f:
    weekly_plan = json.load(f)

# Load or initialize status
if os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, "r") as f:
        task_status = json.load(f)
else:
    task_status = {}

# Initialize session state
if 'done_tasks' not in st.session_state:
    st.session_state.done_tasks = []

if 'notes' not in st.session_state:
    st.session_state.notes = {}

if 'show_done' not in st.session_state:
    st.session_state.show_done = False

# Add new task form
st.sidebar.subheader("Add New Task")
with st.sidebar.form("add_task_form"):
    selected_day = st.selectbox("Select Day", list(weekly_plan.keys()))
    new_task = st.text_input("New Task")
    submitted = st.form_submit_button("Save")
    if submitted and new_task.strip():
        weekly_plan[selected_day].append(new_task.strip())
        with open(PLAN_FILE, "w") as f:
            json.dump(weekly_plan, f)
        st.success(f"Added task '{new_task}' to {selected_day}")
        st.rerun()

st.title("Taha's Weekly Planner")

# Display weekly plan
for day, tasks in weekly_plan.items():
    with st.expander(day):
        for task in tasks:
            task_id = f"{day}_{task}"
            status = task_status.get(task_id, {"check1": False, "check2": False})

            if status["check2"]:
                st.session_state.done_tasks.append(task_id)
                continue

            col1, col2, col3 = st.columns([1, 1, 5])
            with col1:
                new_check1 = st.checkbox("✔1", key=f"{task_id}_1", value=status["check1"])
            with col2:
                new_check2 = False
                if new_check1:
                    new_check2 = st.checkbox("✔2", key=f"{task_id}_2", value=status["check2"])

            with col3:
                color = "#B0C4DE"  # default
                if new_check2:
                    color = "#90EE90"
                elif new_check1:
                    color = "#ADD8E6"

                st.markdown(f"""
                    <div style='background-color: {color}; padding: 10px; border-radius: 10px;'>
                        <strong>{task}</strong>
                    </div>
                """, unsafe_allow_html=True)

            note_key = f"note_{task_id}"
            note = st.text_area("Note", value=st.session_state.notes.get(task_id, ""), key=note_key)
            st.session_state.notes[task_id] = note

            # Update status
            task_status[task_id] = {"check1": new_check1, "check2": new_check2}

# Save task statuses
with open(STATUS_FILE, "w") as f:
    json.dump(task_status, f)

# Done tasks list
st.sidebar.subheader("Done Tasks")
if st.sidebar.button("Show/Hide Done Tasks"):
    st.session_state.show_done = not st.session_state.show_done

if st.session_state.show_done:
    for task_id in st.session_state.done_tasks:
        st.sidebar.write(task_id)

# Reset and Apply buttons
st.sidebar.subheader("Actions")
if st.sidebar.button("Reset All"):
    st.session_state.clear()
    if os.path.exists(STATUS_FILE):
        os.remove(STATUS_FILE)
    st.experimental_rerun()

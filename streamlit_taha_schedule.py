import streamlit as st
import json
import os

st.set_page_config(page_title="Taha's Daily Schedule", layout="wide")

DATA_FILE = "tasks_data.json"
DEFAULT_TASKS = {
    "Saturday": ["Study Math", "Review Physics", "English Practice"],
    "Sunday": ["Revise Chemistry", "Mock Test", "Flashcards"],
    "Monday": ["Computer Class", "Review Notes", "Rest"],
    "Tuesday": ["Math Practice", "Solve Past Papers", "Read Book"],
    "Wednesday": ["Biology", "Group Study", "Summary Notes"],
    "Thursday": ["Mock Exam", "Relaxation", "Plan Next Week"],
    "Friday": ["Programming Class", "Project Work", "Review Week"],
}

COLD_COLOR = "#1F3B4D"
TICKED_COLOR = "#2E8B57"
DONE_COLOR = "#004953"
TEXT_COLOR = "white"

if not os.path.exists(DATA_FILE):
    data = {}
    for day, tasks in DEFAULT_TASKS.items():
        data[day] = {task: {"ticked": 0, "note": ""} for task in tasks}
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
else:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

st.title("**Taha's Daily Schedule**")

selected_day = st.selectbox("Choose a day", list(DEFAULT_TASKS.keys()))

done_tasks = []
active_tasks = []

for task, info in data[selected_day].items():
    if info["ticked"] >= 2:
        done_tasks.append((task, info))
    else:
        active_tasks.append((task, info))

st.subheader(f"Tasks for {selected_day}")

for task, info in active_tasks:
    task_key = f"{selected_day}_{task}"
    col1, col2 = st.columns([0.1, 0.9])

    with col1:
        ticked = st.checkbox("", key=f"check_{task_key}", value=info["ticked"] > 0)

    with col2:
        box_color = TICKED_COLOR if info["ticked"] == 1 else (DONE_COLOR if info["ticked"] >= 2 else COLD_COLOR)
        st.markdown(
            f"<div style='background-color:{box_color};padding:10px;border-radius:5px;color:{TEXT_COLOR}'>{task}</div>",
            unsafe_allow_html=True,
        )
        note = st.text_area("Note", value=info.get("note", ""), height=50, key=f"note_{task_key}")
        info["note"] = note

    # Tick logic
    if ticked and info["ticked"] == 0:
        info["ticked"] = 1
    elif ticked and info["ticked"] == 1:
        info["ticked"] = 2
    elif not ticked:
        info["ticked"] = 0

st.markdown("---")

if done_tasks:
    st.subheader("✅ Completed Tasks")
    for task, info in done_tasks:
        task_key = f"{selected_day}_{task}_done"
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.markdown(
                f"<div style='background-color:{DONE_COLOR};padding:10px;border-radius:5px;color:{TEXT_COLOR}'>{task}</div>",
                unsafe_allow_html=True,
            )
            st.text_area("Note", value=info.get("note", ""), height=50, key=f"note_{task_key}")
        with col2:
            if st.button("Undo", key=f"undo_{task_key}"):
                info["ticked"] = 1

# Save updated data
with open(DATA_FILE, "w") as f:
    json.dump(data, f, indent=4)

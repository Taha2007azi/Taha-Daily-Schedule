import streamlit as st
import json
import os

DATA_FILE = "tasks_data.json"

# Load or initialize data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {}

selected_day = st.selectbox("Select a day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
if selected_day not in data:
    data[selected_day] = {"tasks": [], "done_tasks": []}

st.title(f"Tasks for {selected_day}")

# Input for new task
new_task = st.text_input("Add new task")
if st.button("Add Task"):
    if new_task:
        task_id = f"{selected_day}_{len(data[selected_day]['tasks']) + len(data[selected_day]['done_tasks'])}"
        data[selected_day]["tasks"].append({"id": task_id, "text": new_task, "note": ""})
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

# Show active tasks
st.subheader("Active Tasks")
for idx, task in enumerate(data[selected_day]["tasks"]):
    task_key = task["id"]
    st.markdown(f"**{task['text']}**")
    note_key = f"note_{task_key}"
    
    if note_key not in st.session_state:
        st.session_state[note_key] = task.get("note", "")

    note = st.text_area("Note", height=50, key=note_key)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Done {task_key}"):
            task["note"] = st.session_state[note_key]
            data[selected_day]["done_tasks"].append(task)
            data[selected_day]["tasks"].pop(idx)
            with open(DATA_FILE, "w") as f:
                json.dump(data, f)
            st.experimental_rerun()

# Show done tasks
st.subheader("Completed Tasks")
for idx, task in enumerate(data[selected_day]["done_tasks"]):
    task_key = task["id"]
    st.markdown(f"~~{task['text']}~~")
    st.markdown(f"Note: {task['note']}")
    if st.button(f"Undo {task_key}"):
        data[selected_day]["tasks"].append(task)
        data[selected_day]["done_tasks"].pop(idx)
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        st.experimental_rerun()

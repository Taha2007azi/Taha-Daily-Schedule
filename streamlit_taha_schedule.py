import streamlit as st
import json
import os

DATA_FILE = "taha_schedule_data.json"

# ---------- Load or Initialize Schedule ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

schedule_data = load_data()

# ---------- Get Current Day ----------
days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
selected_day = st.selectbox("Select your day:", days_of_week)

if selected_day not in schedule_data:
    schedule_data[selected_day] = []

# ---------- Display Tasks ----------
st.title(f"Schedule for {selected_day}")
next_tasks = []
done_tasks = []

for idx, task_data in enumerate(schedule_data[selected_day]):
    task_key = f"{selected_day}_{idx}"
    task_text = task_data.get("task", "")
    is_done = task_data.get("done", False)
    note = task_data.get("note", "")

    col1, col2 = st.columns([6, 1])
    with col1:
        color = "#dfffcf" if is_done else "#fff7c2"  # Green if done, yellow if not
        st.markdown(f"<div style='padding: 10px; background-color: {color}; border-radius: 5px;'>{task_text}</div>", unsafe_allow_html=True)
        updated_note = st.text_area("Note", value=str(note), height=50, key=f"note_{task_key}")

    with col2:
        if st.button("Done" if not is_done else "Undo", key=f"done_button_{task_key}"):
            task_data["done"] = not is_done
        task_data["note"] = updated_note

    # Sort done tasks at bottom
    if task_data["done"]:
        done_tasks.append(task_data)
    else:
        next_tasks.append(task_data)

# ---------- Update Display ----------
schedule_data[selected_day] = next_tasks + done_tasks
save_data(schedule_data)

# ---------- Done Section ----------
st.markdown("---")
st.subheader("Completed Tasks")

for task in done_tasks:
    st.markdown(f"- {task['task']}")

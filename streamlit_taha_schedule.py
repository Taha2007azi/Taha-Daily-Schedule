
import streamlit as st
import json
import os

st.set_page_config(page_title="Taha Daily Schedule", layout="wide")

DATA_FILE = "tasks_data.json"

default_tasks = [
    {"day": "Saturday", "tasks": ["Wake up", "Study Math", "Revise Physics"]},
    {"day": "Sunday", "tasks": ["English Practice", "School Homework"]},
    {"day": "Monday", "tasks": ["Programming", "Gym", "Review"]},
    {"day": "Tuesday", "tasks": ["Mock Test", "Analyze Mistakes"]},
    {"day": "Wednesday", "tasks": ["Rest", "Light Reading"]},
    {"day": "Thursday", "tasks": ["Final Revision", "Sleep Early"]},
    {"day": "Friday", "tasks": ["Free Time", "Programming Class"]}
]

# Load tasks from file or initialize
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        task_data = json.load(f)
else:
    task_data = {}
    for day in default_tasks:
        task_data[day["day"]] = {
            task: {"done_count": 0, "note": "", "is_done": False}
            for task in day["tasks"]
        }

st.title("Taha's Daily Schedule")

for day, tasks in task_data.items():
    st.subheader(day)
    cols = st.columns(len(tasks))

    for i, (task, data) in enumerate(tasks.items()):
        with cols[i]:
            done_label = f"✅ {task}" if data["done_count"] > 0 else task
            if data["done_count"] >= 2:
                block_color = "#4a6fa5"  # Custom cold-dark color after 2nd tick
            elif data["done_count"] == 1:
                block_color = "#2e3b4e"
            else:
                block_color = "#1c1c1e"

            with st.container():
                st.markdown(f"<div style='background-color:{block_color}; padding:10px; border-radius:10px;'>", unsafe_allow_html=True)
                checked = st.checkbox(done_label, value=data["is_done"], key=f"{day}_{task}")
                note = st.text_area("Note", value=data.get("note", ""), height=50, key=f"note_{day}_{task}")
                if checked and not data["is_done"]:
                    data["done_count"] += 1
                data["is_done"] = checked
                data["note"] = note
                st.markdown("</div>", unsafe_allow_html=True)

# Save data if any task is confirmed done twice
save_needed = any(data["done_count"] >= 2 for tasks in task_data.values() for data in tasks.values())

if save_needed:
    with open(DATA_FILE, "w") as f:
        json.dump(task_data, f, indent=4)

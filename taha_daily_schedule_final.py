import streamlit as st
import json
import os

st.set_page_config(page_title="Weekly Step Planner", layout="wide")

DATA_FILE = "weekly_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# Style
st.markdown("""
    <style>
        .title {
            font-size: 2.5rem;
            color: #38b6ff;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
        }
        .motiv {
            background: linear-gradient(to right, #38b6ff, #00b4d8);
            padding: 0.8rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 2rem;
        }
        .task-button {
            width: 100%;
            text-align: left;
            padding: 1rem;
            border: none;
            border-radius: 12px;
            margin-bottom: 1rem;
            font-size: 1.2rem;
            font-weight: 500;
            color: #e0e0e0;
            background-color: #2b2d42;
        }
        .task-button-done {
            width: 100%;
            text-align: left;
            padding: 1rem;
            border: none;
            border-radius: 12px;
            margin-bottom: 1rem;
            font-size: 1.2rem;
            font-weight: 500;
            color: white;
            background-color: #007f5f;
        }
        .custom-textarea {
            font-family: 'Courier New', monospace;
            font-size: 1.1rem;
            background-color: #f2f2f2;
            border-radius: 10px;
            padding: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown('<div class="motiv">Every step counts, Taha. Let’s make this week powerful!</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Your Weekly Step Planner</div>', unsafe_allow_html=True)

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
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

# Day selection
selected_day = st.selectbox("Choose a day:", days)
tasks = weekly_plan[selected_day]

if selected_day not in data:
    data[selected_day] = {"done": [False]*len(tasks), "score": 3, "report": ""}
    save_data(data)

# Show task buttons
st.markdown(f"### {selected_day}")
for i, task in enumerate(tasks):
    is_done = data[selected_day]["done"][i]
    css_class = "task-button-done" if is_done else "task-button"
    button_label = f"{task} {'✓' if is_done else ''}"
    if st.button(button_label, key=f"{selected_day}_{i}"):
        data[selected_day]["done"][i] = not is_done
        save_data(data)
        st.rerun()
    st.markdown(f'<div class="{css_class}">{task}</div>', unsafe_allow_html=True)

# When all tasks done
if all(data[selected_day]["done"]):
    st.success(f"All tasks for {selected_day} completed!")

    # Rating
    score = st.slider("Rate your performance today (1–5)", 1, 5, data[selected_day]["score"], key=f"{selected_day}_score")
    data[selected_day]["score"] = score

    # Reflection
    st.markdown("### Daily Reflection:")
    report = st.text_area("Your Notes", value=data[selected_day]["report"], placeholder="Write your thoughts about today...", height=200, key=f"{selected_day}_report")
    data[selected_day]["report"] = report

    if report:
        st.markdown(f"<div class='custom-textarea'>{report}</div>", unsafe_allow_html=True)

    save_data(data)

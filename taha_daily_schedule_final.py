import streamlit as st
import json
import os

st.set_page_config(page_title="Saturday Planner", layout="centered")

# فایل دیتا
DATA_FILE = "data.json"

# ایجاد یا خواندن فایل دیتا
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    data = json.load(f)

if "Saturday" not in data:
    data["Saturday"] = {
        "completed_index": 0,
        "score": None,
        "note": ""
    }

tasks = [
    "05:00 – 05:30: Mind Clearing",
    "05:30 – 06:00: Workout",
    "06:00 – 07:30: English",
    "08:00 – 15:00: School",
    "15:00 – 16:00: Rest",
    "16:00 – 23:00: Study for Konkur"
]

# استایل
st.markdown("""
    <style>
        body { background-color: #1e1e2f; }
        .task-box {
            background-color: #2b2d42;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: #e0e0e0;
            font-weight: 500;
            font-size: 1.2rem;
        }
        .task-done {
            background-color: #007f5f;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            color: white;
            font-weight: 500;
            font-size: 1.2rem;
        }
        .title {
            font-size: 2.5rem;
            color: #38b6ff;
            font-weight: bold;
            text-align: center;
            margin-bottom: 2rem;
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

st.markdown('<div class="title">Saturday Plan</div>', unsafe_allow_html=True)

# نمایش تسک‌ها مرحله‌ای
for i, task in enumerate(tasks):
    if i < data["Saturday"]["completed_index"]:
        st.markdown(f'<div class="task-done">{task} - Done!</div>', unsafe_allow_html=True)
    elif i == data["Saturday"]["completed_index"]:
        st.markdown(f'<div class="task-box">{task}</div>', unsafe_allow_html=True)
        if st.button("Mark as done", key=f"btn_{i}"):
            data["Saturday"]["completed_index"] += 1
            with open(DATA_FILE, "w") as f:
                json.dump(data, f)
            st.rerun()
        break

# اگر همه کارها انجام شده بود
if data["Saturday"]["completed_index"] >= len(tasks):
    st.success("You’ve completed all tasks for Saturday!")

    score = st.slider("Rate your performance today (1–5)", 1, 5, value=data["Saturday"].get("score", 3))
    note = st.text_area("Your Notes", value=data["Saturday"].get("note", ""), height=200)

    # ذخیره امتیاز و یادداشت
    data["Saturday"]["score"] = score
    data["Saturday"]["note"] = note
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

    if note:
        st.markdown(f"<div class='custom-textarea'>{note}</div>", unsafe_allow_html=True)

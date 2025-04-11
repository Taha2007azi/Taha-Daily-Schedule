# Taha Energy Plan - Streamlit App (Daily Planner)

import streamlit as st
import datetime

st.set_page_config(page_title="Taha Energy Plan", layout="wide")

# --- Custom CSS for style ---
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #89CFF0;
            text-align: center;
            margin-bottom: 20px;
        }
        .done {
            background-color: #1f1f1f;
            color: #90ee90;
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
        .task-box {
            background-color: #2e2e2e;
            color: white;
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 10px;
        }
        .blur-button button {
            backdrop-filter: blur(10px);
            border-radius: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Taha Energy Plan</div>', unsafe_allow_html=True)

# --- Task Blocks ---
def task_block(label, key_prefix):
    with st.container():
        st.markdown("<div class='task-box'>", unsafe_allow_html=True)
        check1 = st.checkbox(f"[Check 1] {label}", key=f"{key_prefix}_check1")
        if check1:
            check2 = st.checkbox(f"[Check 2] Confirm done - {label}", key=f"{key_prefix}_check2")
            if check2:
                st.markdown(f"<div class='done'>✅ {label} - Completed</div>", unsafe_allow_html=True)
        note = st.text_area(f"Note for {label}", key=f"{key_prefix}_note")
        st.markdown("</div>", unsafe_allow_html=True)

# --- Tasks of the Day ---

schedule = [
    ("5:00 - 5:15 | Wake up + Music (Chill)", "wake"),
    ("5:15 - 6:00 | Mental reset + stretch + language", "reset"),
    ("6:00 - 6:30 | Breakfast + prepare", "breakfast"),
    ("6:45 | Go to school", "school_go"),
    ("7:00 - 15:00 | School Time", "school"),
    ("15:00 - 16:00 | Rest + chill", "rest"),
    ("16:00 - 18:30 | Light Konkoor Study (Pomodoro style)", "konkoor1"),
    ("18:30 - 19:30 | VRTC Language Class", "language_class"),
    ("19:30 - 20:30 | Dinner + relax", "dinner"),
    ("20:30 - 22:00 | Konkoor or light AI work (video, light coding)", "konkoor2"),
    ("22:00 - 23:30 | Reflect + plan tomorrow", "reflect")
]

for task, key in schedule:
    task_block(task, key)

# --- End of Day Mood/Note ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("How did you feel today?")
st.text_area("Write about your mood, wins, or anything on your mind:", key="daily_feeling")

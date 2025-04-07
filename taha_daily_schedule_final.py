import streamlit as st

st.set_page_config(page_title="Taha's Daily Schedule", layout="centered")

# Colors for days
day_colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

# Highlight color after second checkbox
highlight_color = "#F39C12"

# Schedule
schedule = {
    "Saturday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Study")
    ],
    "Sunday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Monday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 23:00", "Study (10h)")
    ],
    "Tuesday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Wednesday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 23:00", "Study (10h)")
    ],
    "Thursday": [
        ("08:00 – 08:30", "Mind Freeing"),
        ("08:30 – 09:00", "Workout"),
        ("09:00 – 10:30", "English"),
        ("10:30 – 23:00", "Study (10h)")
    ],
    "Friday": [
        ("05:00 – 05:30", "Mind Freeing"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 18:00", "Online Programming Class"),
        ("18:00 – 21:00", "Review")
    ]
}

# Title
st.markdown(
    "<h1 style='text-align: center; color: #F1C40F;'>Taha's Daily Schedule</h1>",
    unsafe_allow_html=True
)

# Choose Day
selected_day = st.selectbox("Select Day", list(schedule.keys()))

# Set background color
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {day_colors[selected_day]};
            color: #ECF0F1;
        }}
        .task-block {{
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# UI
for idx, (time, default_text) in enumerate(schedule[selected_day]):
    task_key = f"{selected_day}_{idx}"

    # حالت اولیه هر تسک
    done1 = st.checkbox("Check 1", key=f"done1_{task_key}")
    done2 = False
    if done1:
        done2 = st.checkbox("Check 2", key=f"done2_{task_key}")

    block_color = highlight_color if done1 and done2 else "rgba(255, 255, 255, 0.05)"

    st.markdown(f"<div class='task-block' style='background-color: {block_color};'>", unsafe_allow_html=True)

    cols = st.columns([1, 3, 2])
    with cols[0]:
        st.markdown(f"<b>{time}</b>", unsafe_allow_html=True)
    with cols[1]:
        st.text_input("Task", value=default_text, key=f"task_{task_key}")
    with cols[2]:
        st.text_area("Note", height=50, key=f"note_{task_key}")

    st.markdown("</div>", unsafe_allow_html=True)

    # اگر هر دو تیک زده شده، نمایش تسک بعدی
    if done1 and done2 and idx + 1 < len(schedule[selected_day]):
        next_time, next_task = schedule[selected_day][idx + 1]
        st.info(f"Next up: **{next_task}** at {next_time}")

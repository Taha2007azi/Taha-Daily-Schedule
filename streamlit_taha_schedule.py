import streamlit as st

# Page setup
st.set_page_config(page_title="Taha's Daily Plan", layout="centered")

# Nice, modern colors
colors = {
    "Saturday": "#1F2833",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#3C4F65"
}

# Weekly schedule (time + default activity)
weekly_schedule = {
    "Saturday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Entrance Exam Study + Breaks")
    ],
    "Sunday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "English Class")
    ],
    "Monday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 23:00", "10-Hour Exam Study")
    ],
    "Tuesday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "English Class")
    ],
    "Wednesday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 23:00", "10-Hour Exam Study")
    ],
    "Thursday": [
        ("8:00 – 8:30", "Mind Clearing"),
        ("8:30 – 9:00", "Workout"),
        ("9:00 – 10:30", "English Study"),
        ("10:30 – 23:00", "10-Hour Exam Study")
    ],
    "Friday": [
        ("5:00 – 5:30", "Mind Clearing"),
        ("5:30 – 6:00", "Workout"),
        ("6:00 – 7:30", "English Study"),
        ("8:00 – 18:00", "Online Programming Class"),
        ("18:00 – 21:00", "Review Study")
    ]
}

# Title
st.markdown("<h1 style='text-align: center; color: #FFD700;'>Taha's Daily Schedule</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D0D3D4;'>You're unstoppable, Taha!</h4>", unsafe_allow_html=True)

selected_day = st.selectbox("Select a day:", list(weekly_schedule.keys()))

# Background color based on the selected day
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {colors[selected_day]};
        color: #F5F5F5;
        font-family: 'Arial', sans-serif;
    }}
    .stCheckbox > div {{
        background-color: rgba(255, 255, 255, 0.05);
        padding: 10px;
        border-radius: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

st.subheader(f"Schedule for {selected_day}")

# Display tasks with checkbox and note
for idx, (time, default_task) in enumerate(weekly_schedule[selected_day]):
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 3, 4])

    with col1:
        st.markdown(f"**{time}**")

    with col2:
        task = st.text_input("Task", value=default_task, key=f"task_{selected_day}_{idx}")
        done = st.checkbox("Done?", key=f"done_{selected_day}_{idx}")

    with col3:
        note_key = f"note_{selected_day}_{idx}"
        note = st.text_area("Note", height=50, key=note_key)

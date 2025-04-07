import streamlit as st

st.set_page_config(page_title="Taha's Daily Plan", layout="centered")

# Weekly schedule
schedule = {
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

st.title("Taha's Daily Schedule")
selected_day = st.selectbox("Select a day:", list(schedule.keys()))
st.subheader(f"Tasks for {selected_day}")

for idx, (time, task) in enumerate(schedule[selected_day]):
    st.markdown(f"**{time}** – {task}")
    st.checkbox("Done?", key=f"{selected_day}_{idx}")
    st.markdown("---")

import streamlit as st

st.set_page_config(page_title="Taha's Daily Schedule", layout="centered")

# Colors per day
colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

# Weekly schedule
weekly_schedule = {
    "Saturday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Study + Lunch/Breaks")
    ],
    "Sunday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "English Class")
    ],
    "Monday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 23:00", "Study (10 hrs) + Breaks")
    ],
    "Tuesday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "English Class")
    ],
    "Wednesday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 23:00", "Study (10 hrs) + Breaks")
    ],
    "Thursday": [
        ("08:00 – 08:30", "Mind release"),
        ("08:30 – 09:00", "Workout"),
        ("09:00 – 10:30", "English"),
        ("10:30 – 23:00", "Study (10 hrs) + Breaks")
    ],
    "Friday": [
        ("05:00 – 05:30", "Mind release"),
        ("05:30 – 06:00", "Workout"),
        ("06:00 – 07:30", "English"),
        ("08:00 – 18:00", "Online Programming Class"),
        ("18:00 – 21:00", "Review (English or Study)")
    ]
}

# Header
st.markdown(
    "<h1 style='text-align: center; color: #F7DC6F;'>Taha's Daily Schedule</h1>",
    unsafe_allow_html=True
)
st.markdown("<h4 style='text-align: center; color: #BDC3C7;'>Go strong, Taha!</h4>", unsafe_allow_html=True)

# Day selector
selected_day = st.selectbox("Select a day:", list(weekly_schedule.keys()))

# Styling
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {colors[selected_day]};
            color: #ECF0F1;
            font-family: 'Tahoma', sans-serif;
        }}
        .stCheckbox > div {{
            background-color: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 8px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader(f"{selected_day} Schedule")

# Display tasks
for idx, (time, default_task) in enumerate(weekly_schedule[selected_day]):
    st.markdown("---")
    cols = st.columns([1, 3, 4])
    with cols[0]:
        st.markdown(f"<b>{time}</b>", unsafe_allow_html=True)
    with cols[1]:
        task = st.text_input("Task", value=default_task, key=f"task_{selected_day}_{idx}")
        done = st.checkbox("Done?", key=f"done_{selected_day}_{idx}")
    with cols[2]:
        note = st.text_area("Note", height=50, key=f"note_{selected_day}_{idx}")

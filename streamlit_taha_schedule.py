import streamlit as st

st.set_page_config(page_title="Taha's Daily Schedule", layout="centered")

# Stylish colors per day
colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

# Weekly plan
weekly_schedule = {
    "Saturday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Study (Exam Prep) + Lunch + Break")
    ],
    "Sunday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Monday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 23:00", "Study Day (10 Hours + Breaks)")
    ],
    "Tuesday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 15:00", "School"),
        ("15:00 – 16:00", "Rest"),
        ("16:00 – 23:00", "Language Class")
    ],
    "Wednesday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 23:00", "Study Day (10 Hours + Breaks)")
    ],
    "Thursday": [
        ("8:00 – 8:30", "Mind Release"),
        ("8:30 – 9:00", "Exercise"),
        ("9:00 – 10:30", "English"),
        ("10:30 – 23:00", "Study Day (10 Hours + Breaks)")
    ],
    "Friday": [
        ("5:00 – 5:30", "Mind Release"),
        ("5:30 – 6:00", "Exercise"),
        ("6:00 – 7:30", "English"),
        ("8:00 – 18:00", "Online Programming Class"),
        ("18:00 – 21:00", "Review Language or Exam Material")
    ]
}

# Title
st.markdown(
    "<h1 style='text-align: center; color: #F1C40F;'>Taha's Daily Schedule</h1>",
    unsafe_allow_html=True
)
st.markdown("<h4 style='text-align: center; color: #BDC3C7;'>Keep Going Strong, Taha!</h4>", unsafe_allow_html=True)

selected_day = st.selectbox("Choose a day:", list(weekly_schedule.keys()))

# Background color based on selected day
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {colors[selected_day]};
            color: #ECF0F1;
            font-family: 'Segoe UI', sans-serif;
        }}
        .stCheckbox > div {{
            background-color: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 8px;
        }}
        textarea, input {{
            background-color: #f4f6f7 !important;
            color: #2c3e50 !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader(f"Schedule for {selected_day}")

# Display each time slot
for idx, (time_slot, default_text) in enumerate(weekly_schedule[selected_day]):
    st.markdown("---")
    cols = st.columns([1, 3, 4])
    with cols[0]:
        st.markdown(f"<b>{time_slot}</b>", unsafe_allow_html=True)
    with cols[1]:
        task = st.text_input("Task", value=default_text, key=f"task_{selected_day}_{idx}")
        done = st.checkbox("Done?", key=f"done_{selected_day}_{idx}")
    with cols[2]:
        note = st.text_area("Note", height=50, key=f"note_{selected_day}_{idx}")

import streamlit as st

# رنگ‌ها برای هر روز
day_colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

highlight_color = "#3498DB"  # رنگ بعد از زدن هر دو تیک

# برنامه هفتگی
schedule = {
    "Saturday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
                 ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"),
                 ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Study")],
    "Sunday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
               ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"),
               ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Language Class")],
    "Monday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
               ("06:00 – 07:30", "English"), ("08:00 – 23:00", "Study (10h)")],
    "Tuesday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
                ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"),
                ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Language Class")],
    "Wednesday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
                  ("06:00 – 07:30", "English"), ("08:00 – 23:00", "Study (10h)")],
    "Thursday": [("08:00 – 08:30", "Mind Freeing"), ("08:30 – 09:00", "Workout"),
                 ("09:00 – 10:30", "English"), ("10:30 – 23:00", "Study (10h)")],
    "Friday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"),
               ("06:00 – 07:30", "English"), ("08:00 – 18:00", "Online Programming Class"),
               ("18:00 – 21:00", "Review")]
}

# عنوان
st.markdown("<h1 style='text-align: center; color: #F1C40F;'>Taha's Daily Schedule</h1>", unsafe_allow_html=True)

# انتخاب روز
selected_day = st.selectbox("Select Day", list(schedule.keys()))

# رنگ پس‌زمینه
st.markdown(f"""
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
""", unsafe_allow_html=True)

# نمایش تسک‌ها
for idx, (time, task_name) in enumerate(schedule[selected_day]):
    key_prefix = f"{selected_day}_{idx}"
    done1 = st.session_state.get(f"done1_{key_prefix}", False)
    done2 = st.session_state.get(f"done2_{key_prefix}", False)

    block_color = highlight_color if done1 and done2 else "rgba(255,255,255,0.05)"
    st.markdown(f"<div class='task-block' style='background-color: {block_color};'>", unsafe_allow_html=True)

    cols = st.columns([1, 3, 2, 2])
    with cols[0]:
        st.markdown(f"<b>{time}</b>", unsafe_allow_html=True)
    with cols[1]:
        st.text_input("Task", value=task_name, key=f"task_{key_prefix}")
    with cols[2]:
        if not done1:
            done1 = st.checkbox("Check 1", key=f"done1_{key_prefix}")
        elif not done2:
            done2 = st.checkbox("Check 2", key=f"done2_{key_prefix}")
        else:
            st.success("Done!")
    with cols[3]:
        st.text_area("Note", key=f"note_{key_prefix}", height=50)

    st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
from datetime import datetime

# رنگ‌ها
COLOR_PENDING = "#1E3A8A"       # آبی تیره
COLOR_CHECKED = "#10B981"       # سبز خفن

# برنامه‌ریزی روزانه
weekly_schedule = {
    "Saturday": ["8:00-9:00 - Task A", "9:00-10:00 - Task B"],
    "Sunday": ["8:00-9:00 - Task C", "9:00-10:00 - Task D"],
    "Monday": ["8:00-9:00 - Task E", "9:00-10:00 - Task F"],
    "Tuesday": ["8:00-9:00 - Task G", "9:00-10:00 - Task H"],
    "Wednesday": ["8:00-9:00 - Task I", "9:00-10:00 - Task J"],
    "Thursday": ["8:00-9:00 - Task K", "9:00-10:00 - Task L"],
    "Friday": ["8:00-9:00 - Task M", "9:00-10:00 - Task N"],
}

st.set_page_config(layout="wide")
st.title("Taha's Daily Schedule")

selected_day = st.selectbox("Choose a day", list(weekly_schedule.keys()))
done_tasks = st.session_state.setdefault("done_tasks", [])

st.markdown("---")
st.subheader(f"Schedule for {selected_day}")
for idx, task in enumerate(weekly_schedule[selected_day]):
    task_key = f"{selected_day}_{idx}"

    # اگر تسک انجام شده باشد
    if task_key in done_tasks:
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(
                f"<div style='padding:10px; background-color:{COLOR_CHECKED}; color:white; border-radius:10px'>{task}</div>",
                unsafe_allow_html=True
            )
        with col2:
            if st.button("↩️", key=f"undo_{task_key}"):
                done_tasks.remove(task_key)
                st.experimental_rerun()
        continue

    # چک‌لیست‌ها
    check1 = st.checkbox("Step 1", key=f"check1_{task_key}")
    check2_visible = check1
    check2 = False
    if check2_visible:
        check2 = st.checkbox("Step 2", key=f"check2_{task_key}")

    # اگر تیک دوم زده شد
    if check2:
        done_tasks.append(task_key)
        st.experimental_rerun()

    # نمایش یادداشت
    st.text_area("Note", value="", height=50, key=f"note_{task_key}")

    # نمایش تسک
    st.markdown(
        f"<div style='padding:10px; background-color:{COLOR_PENDING}; color:white; border-radius:10px'>{task}</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

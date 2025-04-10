import streamlit as st

st.set_page_config(page_title="Custom Weekly Planner", layout="wide")

# رنگ‌بندی خفن
base_color = "#2E3B4E"
active_color = "#4A90E2"
done_color = "#3DDC84"
text_color = "#F5F5F5"

st.markdown(f"""
    <style>
    .block {{
        background-color: {base_color};
        padding: 10px;
        border-radius: 12px;
        margin-bottom: 8px;
        color: {text_color};
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Custom Weekly Planner")

# لیست روزها
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# حالت‌های سشن
if "plan" not in st.session_state:
    st.session_state.plan = {day: [] for day in days}

# فرم اضافه‌کردن تسک
st.sidebar.subheader("Add Task Manually")
with st.sidebar.form("add_task_form"):
    selected_day = st.selectbox("Select Day", days)
    new_task = st.text_input("Enter Task")
    submitted = st.form_submit_button("Add Task")
    if submitted and new_task.strip():
        st.session_state.plan[selected_day].append({
            "title": new_task.strip(),
            "check1": False,
            "check2": False,
            "note": ""
        })
        st.success(f"Task added to {selected_day}")

# نمایش برنامه‌ی ساخته‌شده
for day in days:
    with st.expander(day):
        for i, task in enumerate(st.session_state.plan[day]):
            task_key = f"{day}_{i}"
            col1, col2, col3 = st.columns([1, 1, 6])

            with col1:
                task["check1"] = st.checkbox("✔1", value=task["check1"], key=f"{task_key}_1")
            with col2:
                if task["check1"]:
                    task["check2"] = st.checkbox("✔2", value=task["check2"], key=f"{task_key}_2")
            with col3:
                if task["check2"]:
                    block_color = done_color
                elif task["check1"]:
                    block_color = active_color
                else:
                    block_color = base_color

                st.markdown(f"""
                    <div class="block" style="background-color:{block_color};">
                        <strong>{task['title']}</strong>
                    </div>
                """, unsafe_allow_html=True)

            # یادداشت
            task["note"] = st.text_area("Note", value=task["note"], key=f"{task_key}_note")

# دکمه ریست
st.sidebar.subheader("Actions")
if st.sidebar.button("Reset Planner"):
    st.session_state.plan = {day: [] for day in days}
    st.experimental_rerun()

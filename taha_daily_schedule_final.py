import streamlit as st
import json
import os
import tempfile

st.set_page_config(page_title="Taha's Daily Schedule", layout="centered")

# چک کردن دسترسی به فایل
SAVE_FILE = os.path.join(tempfile.gettempdir(), "schedule_state.json")
use_file = True
try:
    with open(SAVE_FILE, "a") as f:
        pass
except (PermissionError, OSError):
    use_file = False

# توابع ذخیره و بارگذاری برای فایل
def load_state_file():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("فایل ذخیره‌سازی خراب بود و ریست شد.")
                return {}
    return {}

def save_state_file(state):
    with open(SAVE_FILE, "w") as f:
        json.dump(state, f)

# مدیریت state
if use_file:
    saved_state = load_state_file()
else:
    if "saved_state" not in st.session_state:
        st.session_state.saved_state = {}
    saved_state = st.session_state.saved_state

# رنگ‌ها
day_colors = {
    "Saturday": "#1E2A38",
    "Sunday": "#2C3E50",
    "Monday": "#34495E",
    "Tuesday": "#22313F",
    "Wednesday": "#1F3A3D",
    "Thursday": "#2E4053",
    "Friday": "#4A3F35"
}

highlight_color = "#F39C12"

# برنامه روزانه
schedule = {
    "Saturday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"), ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Study")],
    "Sunday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"), ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Language Class")],
    "Monday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 23:00", "Study (10h)")],
    "Tuesday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 15:00", "School"), ("15:00 – 16:00", "Rest"), ("16:00 – 23:00", "Language Class")],
    "Wednesday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 23:00", "Study (10h)")],
    "Thursday": [("08:00 – 08:30", "Mind Freeing"), ("08:30 – 09:00", "Workout"), ("09:00 – 10:30", "English"), ("10:30 – 23:00", "Study (10h)")],
    "Friday": [("05:00 – 05:30", "Mind Freeing"), ("05:30 – 06:00", "Workout"), ("06:00 – 07:30", "English"), ("08:00 – 18:00", "Online Programming Class"), ("18:00 – 21:00", "Review")]
}

# عنوان
st.markdown("<h1 style='text-align: center; color: #F1C40F;'>Taha's Daily Schedule</h1>", unsafe_allow_html=True)

# انتخاب روز
selected_day = st.selectbox("Select Day", list(schedule.keys()))

# تنظیم استایل
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

# رابط کاربری
for idx, (time, default_text) in enumerate(schedule[selected_day]):
    task_key = f"{selected_day}_{idx}"
    
    # اطمینان از اینکه مقادیر پیش‌فرض معتبر باشن
    task_text = saved_state.get(task_key, {}).get("task", default_text) or default_text
    done1 = saved_state.get(task_key, {}).get("done1", False)
    done2 = saved_state.get(task_key, {}).get("done2", False)
    note = saved_state.get(task_key, {}).get("note", "") or ""

    block_color = highlight_color if done1 and done2 else "rgba(255, 255, 255, 0.05)"

    with st.container():
        st.markdown(f"<div class='task-block' style='background-color: {block_color};'>", unsafe_allow_html=True)
        cols = st.columns([1, 3, 2, 2])
        
        with cols[0]:
            st.markdown(f"<b>{time}</b>", unsafe_allow_html=True)
        with cols[1]:
            task_text_new = st.text_input("Task", value=task_text, key=f"task_{task_key}")
        with cols[2]:
            done1_new = st.checkbox("Check 1", value=done1, key=f"done1_{task_key}")
            done2_new = st.checkbox("Check 2", value=done2, key=f"done2_{task_key}")
        with cols[3]:
            note_new = st.text_area("Note", value=note, height=50, key=f"note_{task_key}")
        
        st.markdown("</div>", unsafe_allow_html=True)

        # به‌روزرسانی saved_state
        saved_state[task_key] = {
            "task": task_text_new,
            "done1": done1_new,
            "done2": done2_new,
            "note": note_new
        }

# ذخیره‌سازی
if use_file:
    save_state_file(saved_state)

# دکمه ریست
if st.button("Reset Schedule"):
    saved_state.clear()
    if use_file:
        save_state_file(saved_state)
    st.success("برنامه ریست شد!")

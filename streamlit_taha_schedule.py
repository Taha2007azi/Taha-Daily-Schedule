import streamlit as st

st.set_page_config(page_title="برنامه روزانه طاها", layout="centered")

# رنگ پس‌زمینه برای هر روز
colors = {
    "شنبه": "#1E2A38",
    "یکشنبه": "#2C3E50",
    "دوشنبه": "#34495E",
    "سه‌شنبه": "#22313F",
    "چهارشنبه": "#1F3A3D",
    "پنج‌شنبه": "#2E4053",
    "جمعه": "#4A3F35"
}

# برنامه هفتگی
weekly_schedule = {
    "شنبه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۱۵:۰۰", "مدرسه"),
        ("۱۵:۰۰ – ۱۶:۰۰", "استراحت"),
        ("۱۶:۰۰ – ۲۳:۰۰", "مطالعه کنکور + استراحت و ناهار")
    ],
    "یکشنبه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۱۵:۰۰", "مدرسه"),
        ("۱۵:۰۰ – ۱۶:۰۰", "استراحت"),
        ("۱۶:۰۰ – ۲۳:۰۰", "کلاس زبان")
    ],
    "دوشنبه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۲۳:۰۰", "۱۰ ساعت مطالعه کنکور + استراحت‌ها")
    ],
    "سه‌شنبه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۱۵:۰۰", "مدرسه"),
        ("۱۵:۰۰ – ۱۶:۰۰", "استراحت"),
        ("۱۶:۰۰ – ۲۳:۰۰", "کلاس زبان")
    ],
    "چهارشنبه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۲۳:۰۰", "۱۰ ساعت مطالعه کنکور + استراحت‌ها")
    ],
    "پنج‌شنبه": [
        ("۸:۰۰ – ۸:۳۰", "آزادسازی ذهن"),
        ("۸:۳۰ – ۹:۰۰", "ورزش"),
        ("۹:۰۰ – ۱۰:۳۰", "زبان"),
        ("۱۰:۳۰ – ۲۳:۰۰", "۱۰ ساعت مطالعه کنکور + استراحت‌ها")
    ],
    "جمعه": [
        ("۵:۰۰ – ۵:۳۰", "آزادسازی ذهن"),
        ("۵:۳۰ – ۶:۰۰", "ورزش"),
        ("۶:۰۰ – ۷:۳۰", "زبان"),
        ("۸:۰۰ – ۱۸:۰۰", "کلاس آنلاین برنامه‌نویسی"),
        ("۱۸:۰۰ – ۲۱:۰۰", "مرور زبان یا کنکور")
    ]
}

# استایل کلی
st.markdown(
    "<h1 style='text-align: center; color: #F39C12;'>برنامه روزانه طاها</h1>",
    unsafe_allow_html=True
)
st.markdown("<h4 style='text-align: center; color: #BDC3C7;'>با قدرت جلو برو طاها!</h4>", unsafe_allow_html=True)

selected_day = st.selectbox("انتخاب روز:", list(weekly_schedule.keys()))

# استایل رنگی برای روز انتخاب‌شده
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {colors[selected_day]};
            color: #ECF0F1;
        }}
        .block-container {{
            padding-top: 2rem;
        }}
    </style>
""", unsafe_allow_html=True)

st.subheader(f"برنامه‌ی روز {selected_day}")

# تابع برای ساخت هر آیتم برنامه
def show_task_block(index, time, task_text):
    st.markdown("---")
    cols = st.columns([1, 3, 4])
    with cols[0]:
        st.markdown(f"<b>{time}</b>", unsafe_allow_html=True)
    with cols[1]:
        task = st.text_input("فعالیت", value=task_text, key=f"task_{selected_day}_{index}")
        done = st.checkbox("انجام شد؟", key=f"done_{selected_day}_{index}")
    with cols[2]:
        note = st.text_area("یادداشت", height=50, key=f"note_{selected_day}_{index}")

# اجرای برنامه‌ی روز انتخاب‌شده
for idx, (time_slot, default_text) in enumerate(weekly_schedule[selected_day]):
    show_task_block(idx, time_slot, default_text)

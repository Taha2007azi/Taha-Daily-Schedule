# برنامه‌ی هفتگی
days = ["Select a day", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekly_plan = {
    ...
}

selected_day = st.selectbox("Choose a day:", days)

if selected_day == "Select a day":
    st.markdown("""
        <div style='
            text-align: center;
            font-size: 1.5rem;
            color: #81d4fa;
            margin-top: 3rem;
        '>
            Choose a day to begin planning!<br><br>
            <em>“Success doesn’t come from what you do occasionally, it comes from what you do consistently.”</em>
        </div>
    """, unsafe_allow_html=True)

else:
    tasks = weekly_plan[selected_day]

    # مقداردهی اولیه
    if selected_day not in saved_status_data:
        saved_status_data[selected_day] = [False] * len(tasks)

    # کپی برای تغییرات موقت
    if "temp_status" not in st.session_state:
        st.session_state.temp_status = {}
    if selected_day not in st.session_state.temp_status:
        st.session_state.temp_status[selected_day] = saved_status_data[selected_day][:]

    # نمایش تسک‌ها
    for i, task in enumerate(tasks):
        if st.session_state.temp_status[selected_day][i]:
            st.markdown(f'<div class="task-box task-done">{task}</div>', unsafe_allow_html=True)
        else:
            if st.button(f"✔️ {task}", key=f"{selected_day}_{i}"):
                st.session_state.temp_status[selected_day][i] = True
                st.rerun()

    # --- نوت‌گذاری برای هر روز ---
    st.markdown("### Notes")
    note_key = f"{selected_day}_note"
    if note_key not in saved_status_data:
        saved_status_data[note_key] = ""

    note_text = st.text_area("Write your daily report or notes here:", value=saved_status_data[note_key], height=150)

    # --- دکمه‌های Apply و Reset ---
    with st.form(key="action_form"):
        col1, col2 = st.columns(2)
        with col1:
            apply_click = st.form_submit_button(label="✅ Apply")
        with col2:
            reset_click = st.form_submit_button(label="❌ Reset")

        if apply_click:
            saved_status_data[selected_day] = st.session_state.temp_status[selected_day][:]
            saved_status_data[note_key] = note_text
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.success("Changes and note saved!")

        if reset_click:
            st.session_state.temp_status[selected_day] = [False] * len(tasks)
            saved_status_data[selected_day] = [False] * len(tasks)
            saved_status_data[note_key] = ""
            if note_key in st.session_state:
                del st.session_state[note_key]
            with open(DATA_FILE, "w") as f:
                json.dump(saved_status_data, f)
            st.rerun()

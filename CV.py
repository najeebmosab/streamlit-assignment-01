import streamlit as st

# إعداد الصفحة
st.set_page_config(
    page_title="بطاقتي المهنية",
    page_icon="🪪",
    layout="centered"
)

# عنوان التطبيق والتعليمات
st.title("🪪 بطاقتي المهنية")
st.markdown("أنشئ **سيرة ذاتية مختصرة** تعرض دراستك ومهاراتك.")

st.info("أكمل معلوماتك، ثم اضغط زر عرض السيرة الذاتية.")

# حفظ آخر بطاقة صحيحة خلال الجلسة
if "cv_data" not in st.session_state:
    st.session_state.cv_data = None

# نموذج إدخال المعلومات
with st.form("cv_form"):
    st.subheader("① المعلومات الشخصية")

    name = st.text_input(
        "الاسم الكامل",
        placeholder="مثال: مصعب نجيب",
        max_chars=80
    )

    headline = st.text_input(
        "المسمّى المهني",
        placeholder="مثال: مطوّر برمجيات",
        max_chars=120
    )

    age = st.slider(
        "العمر",
        min_value=17,
        max_value=80,
        value=25
    )

    st.divider()
    st.subheader("② الدراسة")

    # عرض حقول الدراسة في عمودين
    major_col, gpa_col = st.columns(2)

    with major_col:
        major = st.selectbox(
            "التخصص",
            [
                "هندسة البرمجيات",
                "علوم الحاسوب",
                "الذكاء الاصطناعي",
                "الهندسة",
                "الرياضيات",
                "تخصص آخر"
            ]
        )

    with gpa_col:
        gpa = st.number_input(
            "المعدل من 4",
            min_value=0.0,
            max_value=4.0,
            value=3.0,
            step=0.1,
            format="%.1f"
        )

    st.divider()
    st.subheader("③ المهارات والنبذة")

    skills = st.multiselect(
        "مهاراتك",
        [
            "Python",
            "تحليل البيانات",
            "Machine Learning",
            "Angular",
            "C#",
            "SQL",
            "Git",
            "التواصل",
            "العمل الجماعي"
        ]
    )

    bio = st.text_area(
        "نبذة عنك",
        placeholder="اكتب عن دراستك وخبرتك وأهدافك المهنية.",
        height=150,
        max_chars=1000
    )

    ready = st.checkbox("راجعت معلوماتي وأنا جاهز لعرض البطاقة")

    st.caption("الاسم والنبذة وتأكيد المراجعة مطلوبة.")

    submitted = st.form_submit_button(
        "عرض سيرتي الذاتية ✨",
        use_container_width=True
    )

# التحقق من المعلومات عند إرسال النموذج
if submitted:
    if not name.strip():
        st.error("اكتب اسمك الكامل أولًا.")

    elif not bio.strip():
        st.error("اكتب نبذة قصيرة عنك.")

    elif not ready:
        st.warning("أكّد مراجعة المعلومات قبل عرض البطاقة.")

    else:
        st.session_state.cv_data = {
            "name": name.strip(),
            "headline": headline.strip(),
            "age": age,
            "major": major,
            "gpa": gpa,
            "skills": skills,
            "bio": bio.strip()
        }

        st.success("تم إنشاء بطاقتك المهنية بنجاح!")

# عرض آخر بطاقة تم إنشاؤها بنجاح
if st.session_state.cv_data is not None:
    cv = st.session_state.cv_data

    st.divider()
    st.subheader("معاينة السيرة الذاتية")
    st.caption("لتحديث البطاقة، عدّل المعلومات وأرسل النموذج مجددًا.")

    with st.container(border=True):
        st.caption("الملف المهني")
        st.subheader(cv["name"])

        if cv["headline"]:
            st.write(cv["headline"])

        st.divider()

        st.markdown("#### 🎓 الدراسة")
        st.write(cv["major"])

        age_metric, gpa_metric = st.columns(2)

        with age_metric:
            st.metric("العمر", str(cv["age"]) + " سنة")

        with gpa_metric:
            st.metric("المعدل من 4", format(cv["gpa"], ".1f"))

        st.divider()

        st.markdown("#### 👤 نبذة عني")
        st.write(cv["bio"])

        if cv["skills"]:
            st.divider()
            st.markdown("#### 🛠️ المهارات")

            for skill in cv["skills"]:
                st.write("•", skill)

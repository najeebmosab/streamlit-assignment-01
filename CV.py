import streamlit as st

# إعداد الصفحة — يوضع قبل عناصر الواجهة
st.set_page_config(
    page_title="بطاقتي المهنية",
    page_icon="🪪",
    layout="centered"
)

# عنوان التطبيق وتعليماته
st.title("🪪 بطاقتي المهنية")
st.markdown(
    "حوّل معلوماتك إلى **بطاقة تعريف مهنية** مرتّبة."
)

st.info(
    "أكمل النموذج ثم اضغط «عرض سيرتي الذاتية». "
    "لن تُعرض البطاقة قبل إرسال النموذج."
)

# حفظ البطاقة حتى تبقى ظاهرة عند إعادة تشغيل الصفحة تفاعليًا
if "cv_data" not in st.session_state:
    st.session_state.cv_data = None

# النموذج يجمع المدخلات ويرسلها عند الضغط على Submit
with st.form("cv_form"):

    st.subheader("① المعلومات الشخصية")

    name = st.text_input(
        "الاسم الكامل",
        placeholder="مثال: مصعب نجيب",
        max_chars=80
    )

    headline = st.text_input(
        "المسمّى المهني أو المجال المستهدف",
        placeholder="مثال: مطوّر واجهات أمامية | طالب ذكاء اصطناعي",
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

    # توزيع حقول الدراسة على عمودين
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

    # عنصر إضافي يسمح باختيار عدة مهارات
    skills = st.multiselect(
        "المهارات",
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
        ],
        help="اختَر المهارات التي تعبّر عن خبرتك."
    )

    bio = st.text_area(
        "نبذة عنك",
        placeholder=(
            "اكتب جملتين أو ثلاثًا عن دراستك، "
            "خبرتك، وما تطمح لتحقيقه."
        ),
        height=150,
        max_chars=1000
    )

    ready = st.checkbox(
        "راجعت معلوماتي وأنا جاهز لعرض البطاقة"
    )

    st.caption("الاسم والنبذة وتأكيد المراجعة مطلوبة.")

    # زر إرسال النموذج
    submitted = st.form_submit_button(
        "عرض سيرتي الذاتية ✨",
        use_container_width=True
    )

# التحقق من المدخلات بعد الضغط على الزر
if submitted:

    if not name.strip():
        st.error("اكتب الاسم الكامل أولًا.")

    elif not bio.strip():
        st.error("اكتب نبذة قصيرة عنك.")

    elif not ready:
        st.warning("أكّد مراجعة المعلومات قبل عرض البطاقة.")

    else:
        # حفظ نسخة من المعلومات المرسلة
        # البطاقة تعرض آخر إرسال صحيح فقط
        st.session_state.cv_data = {
            "name": name.strip(),
            "headline": headline.strip(),
            "age": age,
            "major": major,
            "gpa": gpa,
            "skills": skills,
            "bio": bio.strip()
        }

        st.success("تم إنشاء سيرتك الذاتية بنجاح!")

# عرض البطاقة عند وجود معلومات محفوظة
if st.session_state.cv_data is not None:

    cv = st.session_state.cv_data

    st.divider()
    st.subheader("معاينة السيرة الذاتية")
    st.caption(
        "هذه آخر نسخة أرسلتها بنجاح. "
        "لتحديثها، عدّل النموذج واضغط الزر مجددًا."
    )

    # حاوية بإطار تجمع عناصر البطاقة
    with st.container(border=True):

        st.caption("PERSONAL PROFILE · الملف

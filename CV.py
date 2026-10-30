import streamlit as st

st.title("بطاقتي المهنية")
st.write("عرّف عن نفسك وأنشئ سيرة ذاتية مختصرة.")

st.markdown("""
### خطوات إنشاء البطاقة
1. أدخل معلوماتك.
2. اكتب نبذة عن دراستك ومهاراتك.
3. اضغط **عرض سيرتي الذاتية**.
""")

st.info("استخدم معلومات ترغب بعرضها في بطاقتك.")

name = st.text_input("الاسم الكامل")

age = st.slider(
    "العمر",
    min_value=17,
    max_value=80,
    value=25
)

major = st.selectbox(
    "التخصص",
    ["هندسة البرمجيات", "علوم الحاسوب", "الذكاء الاصطناعي", "تخصص آخر"]
)

gpa = st.number_input(
    "المعدل من 4",
    min_value=0.0,
    max_value=4.0,
    value=3.0,
    step=0.1
)

bio = st.text_area("نبذة عنك وعن مهاراتك")

if st.button("عرض سيرتي الذاتية"):
    if not name.strip():
        st.warning("اكتب اسمك أولًا.")

    elif not bio.strip():
        st.warning("اكتب نبذة عنك أولًا.")

    else:
        st.success("تم إنشاء بطاقتك المهنية!")

        st.markdown("---")
        st.markdown("## بطاقتي المهنية")

        st.markdown(f"### {name}")
        st.markdown(f"**العمر:** {age}")
        st.markdown(f"**التخصص:** {major}")
        st.markdown(f"**المعدل:** {gpa:.1f} / 4.0")

        st.markdown("### نبذة عني")
        st.write(bio)

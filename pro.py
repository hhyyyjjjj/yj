import streamlit as st

st.set_page_config(page_title="유진님의 프로필", page_icon="💁‍♀️")

st.title("🙋‍♀️ 유진님의 프로필")
st.image("https://i.imgur.com/Z7AzH2c.jpg", width=150)  # 원하는 이미지 링크로 바꿔

st.subheader("🌟 소개")
st.write("""
- 육아 중인 부사관
- 아기 이름은 이안 👶
- 자전거 매니아, 넷플릭스 덕후
- 두 마리 강아지 엄마 🐶🐶
""")

st.subheader("📱 SNS")
st.markdown("[Instagram](https://instagram.com)")
st.markdown("[YouTube](https://youtube.com)")

st.subheader("📝 하고 싶은 말")
st.text_area("방명록 남겨주세요!")


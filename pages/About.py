# pages/About.py
import streamlit as st

st.set_page_config(page_title="📄 About ChessMaster", layout="centered")
st.title("📄 About ChessMaster")

st.markdown("""
<style>
@keyframes fadeIn {
  from {opacity: 0;}
  to {opacity: 1;}
}
.about-section {
  animation: fadeIn 2s ease-in-out;
  font-size: 18px;
  line-height: 1.6;
  color: #2C3E50;
  padding: 10px;
}
</style>

<div class="about-section">
Welcome to **ChessMaster**, a Streamlit-powered chess platform designed to bring strategy, learning, and fun into one immersive experience.

Created by **Gyanankur Baruah**, a passionate data science student and developer, this app blends AI, game logic, and user customization to replicate the feel of professional chess platforms like Chess.com.

---

### 👨‍💻 Creator Bio

I'm a **B.Sc. Data Science** student with a love for intelligent systems, dashboard storytelling, and creative tech. ChessMaster is a personal milestone—combining my skills in Python, Streamlit, and AI integration.

---

### 🔗 Connect With Me

- 💼 [LinkedIn](https://www.linkedin.com/in/gyanankur/)
- 💻 [GitHub](https://github.com/Gyanankur23)
- 📬 Email: gyanankur@example.com

---

Thanks for exploring ChessMaster. May your next move be brilliant!
</div>
""", unsafe_allow_html=True)

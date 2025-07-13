# app.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="♟️ ChessMaster", layout="centered")

# Banner Section
st.markdown("""
<style>
@keyframes slideIn {
  from {opacity: 0; transform: translateY(-20px);}
  to {opacity: 1; transform: translateY(0);}
}
.banner {
  animation: slideIn 1.5s ease-in-out;
  text-align: center;
  font-size: 45px;
  font-weight: bold;
  margin-top: 20px;
  color: #2E4053;
}
.subtitle {
  text-align: center;
  font-size: 22px;
  color: #566573;
  margin-bottom: 20px;
}
</style>

<div class="banner">♟️ Welcome to ChessMaster</div>
<div class="subtitle">Challenge AI bots, solve rating-based puzzles, and customize your board</div>
""", unsafe_allow_html=True)

# Introduction
st.image("https://upload.wikimedia.org/wikipedia/commons/7/7e/Chess_board_opening_staunton.jpg", caption="Let the games begin!", use_column_width=True)
st.markdown("""
ChessMaster is a dynamic chess app built with Streamlit to bring interactive gameplay, smart AI opponents, and deep puzzle-solving to life.

#### 🔧 Features You'll Find:
- 🧠 Play against **20 bots** with ratings from 400 to 3000  
- 🧩 Solve **rating-based puzzles** to improve your tactics  
- 🎨 Customize **themes, background colors, and board styles**  
- ⏱️ Choose **time controls** or use **pass-and-play** mode  
- 🎮 Fully compliant with **legal moves and piece logic**

Use the sidebar to switch between pages. Let’s make your next move count!
""")

# Credits
st.markdown("Created by **Gyanankur Baruah** — [GitHub](https://github.com/Gyanankur23) | [LinkedIn](https://www.linkedin.com/in/gyanankur/)")

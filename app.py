import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="♟️ ChessMaster",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Custom CSS for Chess.com-like Look ----
st.markdown("""
<style>
@keyframes slideIn {
  from {opacity: 0; transform: translateY(-20px);}
  to {opacity: 1; transform: translateY(0);}
}
.banner {
  animation: slideIn 1.5s ease-in-out;
  text-align: center;
  font-size: 48px;
  font-family: 'Segoe UI', 'Arial', sans-serif;
  font-weight: bold;
  margin-top: 20px;
  color: #2e4053;
  letter-spacing: 2px;
  text-shadow: 1px 2px 8px #ccd6df;
}
.subtitle {
  text-align: center;
  font-size: 22px;
  font-family: 'Segoe UI', 'Arial', sans-serif;
  color: #566573;
  margin-bottom: 28px;
}
hr.custom {
  border: 0;
  height: 2px;
  background: linear-gradient(to right, #83a4d4, #b6fbff);
  margin-top: 22px;
  margin-bottom: 32px;
}
.sidebar .sidebar-content {
  background-color: #f8f9fa !important;
}
</style>

<div class="banner">♟️ Welcome to ChessMaster</div>
<div class="subtitle">Your chess playground: Play bots, puzzles, analysis, and more&mdash;with full customization!</div>
<hr class="custom">
""", unsafe_allow_html=True)

# ---- Banner Image ----
st.image(
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308",
    caption="Let the games begin!",
    use_container_width=True,
)

# ---- App Introduction & Features ----
st.markdown("""
ChessMaster is a fully featured Streamlit chess experience inspired by **chess.com**.  
Enjoy interactive gameplay, smart AI opponents, deep puzzle-solving, and robust customization.

### 🚀 **Features Highlights**
- 🧠 Play against **20 bots** (ratings 400–3000), each with unique style
- 🧩 Solve **rating-based puzzles** and track your progress
- 🎨 Customize **themes, backgrounds, board styles, and piece sets**
- ⏱️ Choose **time controls** or use **pass-and-play** (local multiplayer)
- 🌐 Play **online** with friends or random opponents (coming soon)
- 📊 View **leaderboards, stats, and history**
- 🛠️ Settings page for theme, sound, and account preferences
- 📚 Import/export games (PGN, FEN), run advanced analysis

Use the sidebar to navigate between game modes, puzzles, analysis, leaderboards, and settings.  
**Tip:** Personalize your experience in the Settings page!

""")

# ---- Credits & Social ----
st.markdown("""
---
Created by **Gyanankur Baruah**  
[GitHub](https://github.com/Gyanankur23) | [LinkedIn](https://www.linkedin.com/in/gyanankur/)
""")

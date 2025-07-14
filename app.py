import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="♟️ ChessMaster",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Chess Banner (Chess.com-style) ----
st.markdown("""
<style>
.chess-banner {
    background: linear-gradient(90deg, #f8f9fa 0%, #d6eaff 100%);
    border-radius: 18px;
    box-shadow: 0 6px 20px rgba(44,62,80,0.08);
    padding: 32px 0 16px 0;
    margin: 24px 0;
}
.chess-banner-text {
    font-size: 52px;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-weight: 800;
    color: #2e4053;
    letter-spacing: 2px;
    text-shadow: 1px 2px 8px #b5c5d6;
    text-align: center;
}
.chess-banner-sub {
    font-size: 22px;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    color: #1a5276;
    text-align: center;
    margin-top: 10px;
}
</style>
<div class="chess-banner">
  <div class="chess-banner-text">♟️ ChessMaster Arena</div>
  <div class="chess-banner-sub">Play, Learn, Analyze &amp; Conquer – Your Chess Journey Starts Here!</div>
</div>
""", unsafe_allow_html=True)

# ---- Banner Image ----
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/7e/Chess_board_opening_staunton.jpg",
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

# ---- Chessboard Section (Demo) ----
st.header("🕹️ Play Chess!")

import chess
from st_chessboard import st_chessboard

if "board" not in st.session_state:
    st.session_state.board = chess.Board()

fen = st_chessboard(st.session_state.board.fen(), key="main_board", width=400)

if fen != st.session_state.board.fen():
    st.session_state.board.set_fen(fen)

st.markdown(f"**Current FEN:** `{st.session_state.board.fen()}`")

# ---- Credits & Social ----
st.markdown("""
---
Created by **Gyanankur Baruah**  
[GitHub](https://github.com/Gyanankur23) | [LinkedIn](https://www.linkedin.com/in/gyanankur/)
""")

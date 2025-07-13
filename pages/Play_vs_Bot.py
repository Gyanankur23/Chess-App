# pages/Play_vs_Bot.py
import streamlit as st
import chess
import chess.engine
import time
from utils.bot_engine import get_bot_move

st.set_page_config(page_title="🤖 Play vs Bot", layout="centered")
st.title("🤖 Play Against AI Bots")

# Bot Rating Selector
bot_rating = st.slider("🧠 Choose Bot Rating (ELO)", min_value=400, max_value=3000, step=100)
time_limit = st.selectbox("⏱️ Choose Time Control", ["No Limit", "1 min", "5 min", "10 min"])

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = chess.Board()
if "history" not in st.session_state:
    st.session_state.history = []

# Display board
st.markdown(f"### Current Position")
st.text(st.session_state.board)

# User Move Input
user_move = st.text_input("Your Move (e.g., e2e4 or Nf3):")
if user_move:
    try:
        move = st.session_state.board.parse_san(user_move)
        st.session_state.board.push(move)
        st.session_state.history.append(f"You: {user_move}")

        # Bot Move
        with st.spinner("Bot is thinking..."):
            bot_move = get_bot_move(st.session_state.board, bot_rating)
            st.session_state.board.push(bot_move)
            st.session_state.history.append(f"Bot: {st.session_state.board.san(bot_move)}")

    except Exception as e:
        st.error(f"Invalid move: {e}")

# Move History
st.markdown("### 📝 Move History")
for move in st.session_state.history:
    st.write(move)

# Reset Button
if st.button("🔄 Reset Game"):
    st.session_state.board = chess.Board()
    st.session_state.history = []

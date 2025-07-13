# pages/Play_vs_Bot.py
import streamlit as st
import chess
from stchess import st_chess
from utils.bot_engine import get_bot_move
from utils.analytics_tracker import update_stat

st.set_page_config(page_title="🤖 Play vs Bot", layout="centered")
st.title("🤖 Play Against AI Bots")

# Bot Rating Selector
bot_rating = st.slider("🧠 Choose Bot Rating (ELO)", min_value=400, max_value=3000, step=100)
time_control = st.selectbox("⏱️ Time Control", ["No Limit", "1 min", "5 min", "10 min"])

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = chess.Board()
if "fen" not in st.session_state:
    st.session_state.fen = st.session_state.board.fen()
if "history" not in st.session_state:
    st.session_state.history = []

# Render chessboard
fen, move = st_chess(fen=st.session_state.fen, theme=st.session_state.get("theme", "green").lower())

# Handle user move
if move:
    try:
        user_move = st.session_state.board.parse_san(move)
        st.session_state.board.push(user_move)
        st.session_state.history.append(f"You: {move}")
        update_stat("total_games")

        # Bot responds
        bot_move = get_bot_move(st.session_state.board, bot_rating)
        st.session_state.board.push(bot_move)
        bot_san = st.session_state.board.san(bot_move)
        st.session_state.history.append(f"Bot: {bot_san}")
        update_stat("bot_wins")

        # Update FEN
        st.session_state.fen = st.session_state.board.fen()

    except Exception as e:
        st.error(f"Invalid move: {e}")

# Move History
st.markdown("### 📝 Move History")
for move in st.session_state.history[-10:]:
    st.write(move)

# Reset Button
if st.button("🔄 Reset Game"):
    st.session_state.board = chess.Board()
    st.session_state.fen = st.session_state.board.fen()
    st.session_state.history = []

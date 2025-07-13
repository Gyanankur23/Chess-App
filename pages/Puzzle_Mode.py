# pages/Puzzle_Mode.py
import streamlit as st
import chess
from utils.puzzle_loader import load_puzzle

st.set_page_config(page_title="🧩 Puzzle Mode", layout="centered")
st.title("🧩 Solve Chess Puzzles")

# Difficulty Selector
difficulty = st.selectbox("🎯 Choose Puzzle Rating", ["400", "800", "1200", "1600", "2000", "2400"])

# Load Puzzle
puzzle = load_puzzle(difficulty)
board = chess.Board(puzzle["fen"])
solution = puzzle["solution"]

# Display Puzzle
st.markdown(f"### Puzzle Position ({difficulty} ELO)")
st.text(board)

# User Move Input
user_move = st.text_input("Your Move (e.g., Nf3):")
if user_move:
    try:
        move = board.parse_san(user_move)
        board.push(move)
        if user_move == solution[0]:
            st.success("✅ Correct! Well played.")
        else:
            st.error("❌ Incorrect. Try again or reset.")
    except Exception as e:
        st.error(f"Invalid move: {e}")

# Reset Button
if st.button("🔄 Load New Puzzle"):
    st.experimental_rerun()

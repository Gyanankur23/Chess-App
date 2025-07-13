# pages/Leaderboard.py
import streamlit as st
from utils.analytics_tracker import load_stats

st.set_page_config(page_title="🏆 Leaderboard", layout="centered")
st.title("🏆 Your Game Stats")

stats = load_stats()
st.metric("Puzzles Solved", stats.get("puzzles_solved", 0))
st.metric("Bot Wins", stats.get("bot_wins", 0))
st.metric("Total Games Played", stats.get("total_games", 0))

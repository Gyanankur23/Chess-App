import streamlit as st
from stchess import st_chess

st.set_page_config(page_title="♟️ Chess Board", layout="centered")

st.title("♟️ Real Chess Board")

# Display board with default theme
fen, move = st_chess(fen="start", theme="green")

st.write("Current FEN:", fen)
st.write("Last Move:", move)

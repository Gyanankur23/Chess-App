# pages/Interactive_Board.py
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="♟️ Interactive Chess", layout="centered")
st.title("♟️ Interactive Chess Board")

# Load HTML board
with open("board.html", "r") as file:
    board_html = file.read()

components.html(board_html, height=500)

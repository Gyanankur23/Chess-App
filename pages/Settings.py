# pages/Settings.py
import streamlit as st
from utils.theme_manager import apply_theme

st.set_page_config(page_title="🎨 Settings", layout="centered")
st.title("🎨 Customize Your Chess Experience")

# 🎭 Board Theme Options
board_options = [
    "Classic", "Dark", "Blue", "Wood", "Glass",
    "Emerald", "Purple Dream", "Lava", "Sky", "Monochrome"
]

# ♟️ Piece Color Options
piece_options = [
    "White & Black", "Gold & Silver", "Red & Blue", "Emerald & Navy",
    "Purple & Teal", "Sunset & Ocean", "Coral & Gray", "Sky & Earth",
    "Pixel Contrast", "Vintage Sepia"
]

# 🧠 User Selections
theme = st.selectbox("🎭 Choose Board Theme", board_options)
piece_color = st.selectbox("♟️ Choose Piece Color Set", piece_options)
background = st.color_picker("🖼️ Pick Background Color", "#F0F0F0")

# 💾 Save to session
st.session_state["theme"] = theme
st.session_state["piece_color"] = piece_color
st.session_state["background"] = background

# 🎨 Apply Theme
apply_theme(theme, piece_color, background)

# 🔍 Preview Settings
st.markdown("### 🧪 Preview")
st.markdown(f"- **Board Theme:** {theme}")
st.markdown(f"- **Piece Colors:** {piece_color}")
st.markdown(f"- **Background:** {background}")

# 🔄 Reset Button
if st.button("🔄 Reset to Default"):
    st.session_state["theme"] = "Classic"
    st.session_state["piece_color"] = "White & Black"
    st.session_state["background"] = "#F0F0F0"
    st.experimental_rerun()

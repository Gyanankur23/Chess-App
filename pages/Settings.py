# pages/Settings.py
import streamlit as st

st.set_page_config(page_title="🎨 Settings", layout="centered")
st.title("🎨 Customize Your Chess Experience")

# Theme Selector
theme = st.selectbox("🎭 Choose Board Theme", ["Classic", "Dark", "Blue", "Wood", "Glass"])
piece_color = st.radio("♟️ Choose Piece Color", ["White & Black", "Gold & Silver", "Red & Blue"])
background = st.color_picker("🖼️ Pick Background Color", "#F0F0F0")

# Save Preferences
st.session_state["theme"] = theme
st.session_state["piece_color"] = piece_color
st.session_state["background"] = background

# Preview
st.markdown("### 🧪 Preview Settings")
st.markdown(f"- **Theme:** {theme}")
st.markdown(f"- **Piece Color:** {piece_color}")
st.markdown(f"- **Background:** {background}")

# Reset Button
if st.button("🔄 Reset to Default"):
    st.session_state["theme"] = "Classic"
    st.session_state["piece_color"] = "White & Black"
    st.session_state["background"] = "#F0F0F0"
    st.experimental_rerun()

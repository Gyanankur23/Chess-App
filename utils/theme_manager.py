# utils/theme_manager.py
import streamlit as st

def apply_theme(theme: str, piece_color: str, background: str):
    """Injects custom CSS based on selected board theme and piece colors."""
    
    # 🎲 Board Styles
    board_styles = {
        "Classic": "#F0D9B5",
        "Dark": "#1C1C1C",
        "Blue": "#A9CCE3",
        "Wood": "#DEB887",
        "Glass": "#E5E8E8",
        "Emerald": "#2ECC71",
        "Purple Dream": "#BB8FCE",
        "Lava": "#E74C3C",
        "Sky": "#AED6F1",
        "Monochrome": "#D5D8DC"
    }

    # 🧩 Piece Color Sets
    piece_styles = {
        "White & Black": ("#FFFFFF", "#000000"),
        "Gold & Silver": ("#FFD700", "#C0C0C0"),
        "Red & Blue": ("#FF4136", "#0074D9"),
        "Emerald & Navy": ("#2ECC71", "#2E4053"),
        "Purple & Teal": ("#8E44AD", "#1ABC9C"),
        "Sunset & Ocean": ("#E67E22", "#3498DB"),
        "Coral & Gray": ("#F08080", "#7F8C8D"),
        "Sky & Earth": ("#85C1E9", "#7D6608"),
        "Pixel Contrast": ("#FDFEFE", "#17202A"),
        "Vintage Sepia": ("#A0522D", "#3E2723")
    }

    # Defaults if missing
    board_color = board_styles.get(theme, "#F0D9B5")
    white_piece, black_piece = piece_styles.get(piece_color, ("#FFFFFF", "#000000"))

    # 🖼️ Inject Styling
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {background};
    }}
    .chess-board {{
        background-color: {board_color};
        border: 2px solid #333;
        box-shadow: 0px 2px 20px rgba(0,0,0,0.3);
    }}
    .piece-white {{
        color: {white_piece};
        font-weight: bold;
    }}
    .piece-black {{
        color: {black_piece};
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

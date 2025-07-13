# utils/bot_engine.py
import chess
import chess.engine

# Path to Stockfish binary (adjust if needed)
STOCKFISH_PATH = "stockfish"  # Ensure it's installed and in PATH

# Map ELO rating to Stockfish depth
def rating_to_depth(rating):
    if rating <= 600:
        return 1
    elif rating <= 1000:
        return 5
    elif rating <= 1400:
        return 10
    elif rating <= 1800:
        return 15
    elif rating <= 2200:
        return 20
    elif rating <= 2600:
        return 25
    else:
        return 30

# Get bot move based on board and rating
def get_bot_move(board: chess.Board, rating: int) -> chess.Move:
    depth = rating_to_depth(rating)
    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        result = engine.play(board, chess.engine.Limit(depth=depth))
        return result.move

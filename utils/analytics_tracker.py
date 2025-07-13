# utils/analytics_tracker.py
import json
import os

STATS_FILE = "data/stats.json"

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return {"puzzles_solved": 0, "bot_wins": 0, "total_games": 0}

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

def update_stat(key):
    stats = load_stats()
    stats[key] = stats.get(key, 0) + 1
    save_stats(stats)

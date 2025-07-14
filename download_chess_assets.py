import os
import requests
from tqdm import tqdm

# ==== Configuration ====
PIECE_SETS = {
    # Lichess open source SVG sets
    "cburnett": "https://github.com/lichess-org/lila/tree/master/public/piece/standard",
    "celtic": "https://github.com/lichess-org/lila/tree/master/public/piece/celtic",
    "alpha": "https://github.com/lichess-org/lila/tree/master/public/piece/alpha",
    "fantasy": "https://github.com/lichess-org/lila/tree/master/public/piece/fantasy",
    "fresca": "https://github.com/lichess-org/lila/tree/master/public/piece/fresca",
    "pirouetti": "https://github.com/lichess-org/lila/tree/master/public/piece/pirouetti",
    "condal": "https://github.com/lichess-org/lila/tree/master/public/piece/condal",
    # Add more sets from https://github.com/lichess-org/lila/tree/master/public/piece
}

BOARD_THEMES = [
    # Lichess board backgrounds (SVG PNG)
    "https://github.com/lichess-org/lila/tree/master/public/board/svg",
    "https://github.com/lichess-org/lila/tree/master/public/board/png",
]

SOUNDS = [
    # Direct links to Lichess sounds (MP3/OGG)
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/move.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/capture.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/notify.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/win.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/lose.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/draw.mp3",
    "https://raw.githubusercontent.com/lichess-org/lila/master/public/sound/check.mp3",
    # Add more from https://github.com/lichess-org/lila/tree/master/public/sound
]

ICONS = [
    # Example Material Icons (SVG)
    "https://raw.githubusercontent.com/google/material-design-icons/master/svg/production/ic_settings_24px.svg",
    "https://raw.githubusercontent.com/google/material-design-icons/master/svg/production/ic_person_24px.svg",
    "https://raw.githubusercontent.com/google/material-design-icons/master/svg/production/ic_chat_24px.svg",
]

# ==== Utility Functions ====
def download_file(url, dest_folder, filename=None):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    if filename is None:
        filename = os.path.basename(url)
    dest_path = os.path.join(dest_folder, filename)
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dest_path, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=8192), desc=f"Downloading {filename}"):
                    f.write(chunk)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_github_folder(github_url, dest_folder):
    """
    Download all files from a public GitHub folder using the GitHub API.
    Example: 'https://github.com/lichess-org/lila/tree/master/public/piece/standard'
    """
    import re
    api_url = github_url.replace("github.com", "api.github.com/repos").replace("/tree/", "/contents/")
    # Remove any trailing slash
    api_url = api_url.rstrip('/')
    try:
        resp = requests.get(api_url)
        resp.raise_for_status()
        files = resp.json()
        for file in files:
            if file["type"] == "file":
                download_file(file["download_url"], dest_folder)
    except Exception as e:
        print(f"Failed to download folder {github_url}: {e}")

# ==== Download Assets ====
def main():
    print("Downloading Chess Piece Sets...")
    for set_name, set_url in PIECE_SETS.items():
        print(f"Downloading piece set: {set_name}")
        download_github_folder(set_url, f"assets/pieces/{set_name}")

    print("\nDownloading Board Themes...")
    for board_url in BOARD_THEMES:
        theme_type = "svg" if board_url.endswith("/svg") else "png"
        download_github_folder(board_url, f"assets/boards/{theme_type}")

    print("\nDownloading Sounds...")
    for sound_url in SOUNDS:
        download_file(sound_url, "assets/sounds")

    print("\nDownloading Icons...")
    for icon_url in ICONS:
        download_file(icon_url, "assets/icons")

if __name__ == "__main__":
    main()

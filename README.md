# Chess Game Animation

This project generates an **animated GIF** of a chess game from a **PGN** file.

## Features
- Parses PGN files to extract moves
- Generates board images for each move
- Creates an animated GIF showing the game's progression

## Installation

### **Conda (Recommended)**
If you use **Conda**, install dependencies in one step:

```sh
conda create -n chess-animation -c conda-forge cairo pango gdk-pixbuf ffmpeg python-chess pillow imageio cairosvg
conda activate chess-animation
```

### **Using Poetry**
If you're using **Poetry**, install Python dependencies with:
```sh
poetry add python-chess pillow imageio cairosvg
```

You'll also need to manually install system dependencies:
```sh
sudo apt install libcairo2-dev libjpeg-dev libgif-dev  # Debian/Ubuntu
brew install cairo                                     # macOS
```

### **Manual Installation with pip**
If you prefer **pip**, install dependencies manually:
```sh
pip install python-chess pillow imageio cairosvg
```

## Usage

1. Save a **PGN** file (e.g., `game.pgn`).
2. Run the script:

```sh
python -m chessanimate game.pgn
```

3. The output will be saved as `chess_animation.gif`.
```

## Dependencies
- **python-chess** - Chess board rendering & PGN parsing
- **Pillow** - Image processing
- **imageio** - GIF creation
- **cairosvg** - Converts SVG to PNG
- **Cairo** - Required for SVG rendering

[comment]: <> (## Output Example)
[comment]: <> ()
[comment]: <> (![Example GIF](chess_animation.gif))

## License

MIT License.

---

Author: [DJ Stomp](https://github.com/djstompzone)
Repo: [GitHub - chessanimate](https://github.com/djstompzone/chessanimate)

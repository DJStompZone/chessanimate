#!/usr/bin/env python3


import argparse
import sys
from chessanimate import animate  # git+https://github.com/djstompzone/chessanimate.git

def main():
    parser = argparse.ArgumentParser(
        description="Generate an animated GIF from a PGN file."
    )
    parser.add_argument("pgn_file", help="Path to the PGN file")
    parser.add_argument(
        "-o", "--output", default="chess_animation.gif", help="Output GIF filename"
    )
    parser.add_argument(
        "-d", "--duration", type=int, default=500, help="Frame duration in milliseconds"
    )

    args = parser.parse_args()

    try:
        animate.generate_chess_animation(args.pgn_file, args.output, args.duration)
        print(f"GIF saved as {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

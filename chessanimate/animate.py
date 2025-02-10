import io
import sys
import imageio

from PIL import Image
import cairosvg
import chess
import chess.pgn
import chess.svg

def svg_to_png(svg_data):
    png_data = cairosvg.svg2png(bytestring=svg_data)
    return Image.open(io.BytesIO(png_data))

def generate_chess_animation(pgn_file, output_gif="chess_animation.gif", duration=500):
    game = chess.pgn.read_game(open(pgn_file))
    board = game.board()

    images = []

    for move in game.mainline_moves():
        board.push(move)
        svg_data = chess.svg.board(board, size=350)
        img = svg_to_png(svg_data)
        images.append(img)

    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=duration, loop=0)

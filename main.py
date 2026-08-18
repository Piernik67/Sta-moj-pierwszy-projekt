from fastapi import FastAPI
import chess

app = FastAPI()

def get_board(fen: str):
    board = chess.Board(fen)
    return str(board)

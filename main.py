from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import chess

app = FastAPI()

@app.get("/board", response_class=PlainTextResponse)
def get_board(fen: str):
    board = chess.Board(fen)
    return str(board)

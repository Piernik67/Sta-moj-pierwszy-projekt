from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import chess

app = FastAPI()

@app.get("/board", response_class=PlainTextResponse)
def get_board(dwa: str):
    board = chess.Board(dwa)
    return str(board)

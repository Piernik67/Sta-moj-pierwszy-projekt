from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import chess
import uuid

app = FastAPI()

games: dict[str, chess.Board] = {}


@app.post("/board")
def new_game() -> str:
    game_id = str(uuid.uuid4())
    games[game_id] = chess.Board()
    return game_id


@app.get("/board/{game_id}", response_class=PlainTextResponse)
def get_game(game_id: str) -> str:
    try:
        return str(games[game_id])
    except KeyError:
        return f"There is no game with the id: {game_id}"
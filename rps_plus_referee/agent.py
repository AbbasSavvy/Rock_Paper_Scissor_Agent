import random
from google.adk.agents.llm_agent import Agent

def validate_moves(user_move, bomb_used):
    valid_moves = {"rock", "paper", "scissors", "bomb"}

    if user_move not in valid_moves:
        return {'move_valid': False, "reason": "User move is Invalid"}

    if user_move == "bomb" and bomb_used:
        return {"move_valid": False, "reason": "Bomb already used"}

    return {"move_valid": True}


def choose_bot_move(bot_used_bomb):
    if not bot_used_bomb:
        moves = ["rock", "paper", "scissors", "bomb"]
    else:
        moves = ["rock", "paper", "scissors"]

    return random.choice(moves)


def resolve_round(user_move, bot_move):
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"

    if user_move == "bomb":
        return "user"

    what_beats_what = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if bot_move == what_beats_what[user_move]:
        return "user"
    else:
        return "bot"

root_agent = Agent(
    name="rps_plus_referee",
    model="gemini-1.5-flash",
    description=(
        "You are the referee for Rock–Paper–Scissors–Plus.\n"
        "Rules:\n"
        "- Valid moves: rock, paper, scissors, bomb\n"
        "- Bomb can be used once per player\n"
        "- Bomb beats all moves\n\n"
        "You must:\n"
        "1. Validate the user move\n"
        "2. Choose a bot move\n"
        "3. Resolve the round\n"
        "4. Respond ONLY with structured JSON\n\n"
        "Output schema:\n"
        "{\n"
        '  "user_move": string,\n'
        '  "bot_move": string,\n'
        '  "winner": "user" | "bot" | "draw",\n'
        '  "message": string\n'
        "}"
    ),
    tools=[
        validate_moves,
        choose_bot_move,
        resolve_round,
    ],
)
import random

from google.adk import Agent

# Creating function for setting initial state of the game:
def init_state():
    init_dict = {
        "round_number": 1,
        "user_score": 0,
        "bot_score": 0,
        "user_used_bomb": False,
        "bot_used_bomb": False,
        "game_over": False
    }

    return init_dict


def display_rules():
    print("Rock–Paper–Scissors–Plus")
    print("Best of 3 rounds.")
    print("Moves: rock, paper, scissors.")
    print("You may use bomb once; it beats all moves.")
    print("Invalid moves waste the round.")


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


def update_game_state(state, winner, user_move, bot_move):

    if winner == "user":
        state["user_score"] += 1
    elif winner == "bot":
        state["bot_score"] += 1

    if user_move == "bomb":
        state["user_used_bomb"] = True
    elif bot_move == "bomb":
        state["bot_used_bomb"] = True

    state["round_number"] += 1

    if state["round_number"] > 3:
        state["game_over"] = True

    return state


root_agent = Agent(
    name="rps_plus_referee",
    # model="gemini-2.0-flash",
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



def run_game():
    state = init_state()
    display_rules()

    while not state["game_over"]:
        print(f"\nRound {state['round_number']}")
        user_input = input("Your move: ").strip().lower()

        validation = validate_moves(user_input, state["user_used_bomb"])

        if not validation["move_valid"]:
            print(f"Invalid move: {validation['reason']}")
            bot_move = choose_bot_move(state["bot_used_bomb"])
            winner = "bot"
        else:
            bot_move = choose_bot_move(state["bot_used_bomb"])
            winner = resolve_round(user_input, bot_move)

        state = update_game_state(state, winner, user_input, bot_move)

        print("__________________")
        print(f"You Played: {user_input}")
        print(f"Bot played: {bot_move}")
        print(f"Round winner: {winner}")
        print(f"Scores || You: {state['user_score']} || Bot: {state['bot_score']}")


    print("Game Over")

    if state["user_score"] > state["bot_score"]:
        print("Final Result: You Win!")
    elif state["bot_score"] > state["user_score"]:
        print("Final Result: Bot wins")
    else:
        print("Final Result: Draw")

if __name__ == '__main__':
    run_game()
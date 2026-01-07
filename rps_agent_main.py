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





def run_game():
    state = init_state()
    display_rules()

    while not state["game_over"]:
        print(f"\nRound {state['round']}")
        user_input = input("Your move: ").strip().lower()

        validation = validate_moves(user_input, state["user_used_bomb"])

# Creating function for setting initial state of the game:
def init_state():
    init_dict = {
        "round_number": 1,
        "user_score": 0,
        "bot_score": 0,
        "user_used_bomb": False,
        "bot_used_bomb": False
    }


def display_rules():
    print("Rock–Paper–Scissors–Plus")
    print("Best of 3 rounds.")
    print("Moves: rock, paper, scissors.")
    print("You may use bomb once; it beats all moves.")
    print("Invalid moves waste the round.")
    
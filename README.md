# Rock-Paper-Scissors-Plus - Design Overview

# Rock–Paper–Scissors–Plus — Design Overview

## Table of Contents

- [State Model](#state-model)
- [Agent / Tool Design](#agent--tool-design)
- [Tradeoffs](#tradeoffs)
- [Future Improvements](#future-improvements)
- [How to Run](#how-to-run)



---

## State Model
The game uses a **single mutable state dictionary** to represent the entire game lifecycle.  
The state contains:

- `round_number`: Tracks progression (max 3 rounds)
- `user_score`, `bot_score`: Keep score of user and bot for each round
- `user_used_bomb`, `bot_used_bomb`: To make sure bomb is only used once per player
- `game_over`: Used to show termination of the game loop

All state transitions occur explicitly in a single function (`update_game_state`), making the game easy to reason about and understand.

---

## Agent / Tool Design

The core game logic is decomposed into the following functions:

- `validate_moves`: Validation of user input and checking whether bomb hasn't been used more than once. 
- `choose_bot_move`: Used to get random bot move.
- `resolve_round`: Used to resolve the round and find a winner for that round.
- `update_game_state`: Used to update the state and check whether the game should continue.

Note: These functions are also registered as tools on a `google.adk.Agent` instance. However, the agent is not used to execute the game loop. Instead, the game runs procedurally to comply with assignment constraints prohibiting API or LLM usage.

This design allows the same logic to be reused in an agentic setting without changing the underlying rules.

---

## Tradeoffs

- The game loop is explicitly coded rather than delegated to an agent, to make sure it is compliant with “no API” rule.
- The bot uses random move selection rather than adaptive or strategic behavior to avoid introducing unnecessary complexity.

---

## Future Improvements

With more time, the following enhancements would be made:


- Allow the agent to drive the gameplay using structured JSON responses.
- Add strategy-aware bot behavior.

---

## How to Run

### Requirements
- **Python 3**
- Optional (only to satisfy the import statement):
  ```bash
  pip install google-adk
  
> **Note:** The game logic does not rely on any LLM at runtime. The pip dependency exists only for reference purposes of the import statement.

### Steps

1. Clone the repository
2. Navigate to the directory containing `rps_agent_main.py`
3. Run the game:
   ```bash
   python rps_agent_main.py
4. Enter your move
    - rock
    - paper
    - scissors
    - bomb
   
The game runs for a maximum of 3 rounds and prints the final result at the end.
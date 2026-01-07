# Rock-Paper-Scissors-Plus - Design Overview

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
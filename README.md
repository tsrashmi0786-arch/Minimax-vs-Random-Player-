# Minimax-vs-Random-Player-

## Game AI Project

This project implements a Tic-Tac-Toe game where an **AI player using the Minimax algorithm** competes against a **Random Player**.

The purpose of this project is to demonstrate how game-playing Artificial Intelligence can make decisions by evaluating possible future moves.

---

##  Project Description

The game consists of two players:

- **Minimax Player (X)** – Uses the Minimax algorithm to choose the best possible move.
- **Random Player (O)** – Selects an available move randomly.

The Minimax player analyzes the possible game states and tries to maximize its chance of winning while minimizing the opponent's chance of winning.

---

## Algorithm Used

### Minimax Algorithm

Minimax is a decision-making algorithm commonly used in two-player games.

The algorithm:

1. Checks the current game state.
2. Generates all possible moves.
3. Simulates each possible move.
4. Assigns a score to each resulting game state.
5. Chooses the move with the best score.
6. Continues until the game reaches a win, loss, or draw.

The scoring system used in this project is:

- **+1** → Minimax Player wins
- **-1** → Random Player wins
- **0** → Draw

---

## Random Player

The Random Player does not use any intelligent strategy.

It:

1. Finds all available positions.
2. Selects one position randomly.
3. Places its symbol on the board.

This allows us to compare an intelligent AI strategy with a random strategy.

---

## Technologies Used

- Python 3
- Minimax Algorithm
- Random Number Generation
- Tic-Tac-Toe Game

---

## Project Structure

```text
Minimax-vs-Random-Player/
│
├── README.md
├── requirements.txt
│
├── src/
│   └── minimax_vs_random.py
│
├── tests/
│   └── test_game.py
│
└── docs/
    ├── report.pdf
    ├── screenshots/
    └── plots/

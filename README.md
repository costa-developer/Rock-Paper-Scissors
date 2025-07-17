# Rock-Paper-Scissors AI Challenge

## Overview

This project implements an advanced Rock-Paper-Scissors (RPS) AI player designed to consistently beat a variety of opponent bots by using adaptive strategies. The goal is to win at least 60% of the games against each bot in a series of matches.

The AI uses:

* Opponent move frequency analysis
* Markov chain pattern prediction
* Reaction detection to opponent counters
* Weighted strategy mixing with controlled randomness

---

## Files

* `RPS.py`
  Contains the `player` function — the AI agent that selects moves based on opponent history.

* `main.py`
  Runs tests by playing the AI against various opponent bots for multiple rounds.

* `RPS_game.py`
  The game engine provided by the challenge environment. Do not modify.

---

## How to Run Locally

1. **Ensure all files** (`RPS.py`, `main.py`, `RPS_game.py`) are in the same directory.

2. **Open your terminal** and navigate to the project directory:

   ```bash
   cd /path/to/project-folder
   ```

3. **Run the test script:**

   ```bash
   python main.py
   ```

4. The program will simulate 1000 games against each opponent bot and output the results. Aim for at least 60% wins per bot.

---

## Player Function Details

* `player(prev_play, opponent_history=[])`

  * `prev_play` (str): Opponent's last move ("R", "P", "S") or `""` on the first move.
  * `opponent_history` (list): Tracks all previous opponent moves (managed internally).

* Returns the next move as `"R"`, `"P"`, or `"S"`.

* Uses multiple adaptive strategies and randomness to maximize win rate.

---

## Dependencies

* Python 3.6+
* Standard library only (no external packages needed).

---

## Notes

* The AI uses internal state stored in function attributes to maintain move history.

* Modify or enhance the `player` function in `RPS.py` to experiment with other strategies.

* The `main.py` script can be customized to run different numbers of games or include verbose output for detailed logs.

---

## Contact

For questions or improvements, reach out to the project maintainer.



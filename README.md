# 🎲 Dice Game in Python

This project is a simple command-line-based dice game built in Python. The game allows 2 to 4 players to compete against each other to reach a target score of 50 by rolling a six-sided die. Players take turns, and the game continues until one player scores 50 or more.

# How It Works:
- Players take turns automatically rolling until they either roll a 1 or decide to stop when close to winning.
- Player scores are updated at the end of each turn.
- Once any player reaches the target score, the game announces the winner.

## 📜 Rules of the Game

- Each player takes turns rolling a six-sided die.
- If a player rolls any number between 2 and 6, that value is added to their round score, and they can choose to roll again.
- If a player rolls a 1, their round ends immediately, and their round score is reset to 0 for that turn.
- A player's round score is added to their total score at the end of their turn (if they didn’t roll a 1).
- The first player to reach a total score of 50 or more wins the game.
- In case of a tie (if more than one player reaches the max score in the same round), the game announces a tie between those players.

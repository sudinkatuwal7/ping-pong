# 🏓 Python's Ping Pong Game

A classic **Ping Pong game** built in **Python** using **Turtle graphics** and **Object-Oriented Programming (OOP)** principles.  
Play a fun, interactive game while exploring clean, modular Python code! 🎮🐍

---

## ✨ Features

- **Two-player gameplay** on the same keyboard
- **Dynamic ball mechanics**
  - Bounces off paddles
  - Bounces off walls
  - **Increases speed after hitting a paddle ⚡**
  - Resets to normal speed when a player misses
- **Real-time scoreboard**
  - Tracks left and right player scores
- **Clean OOP structure**
  - Separate classes for `Paddle`, `Ball`, and `Scoreboard`
  - Easy to read, extend, and modify

---

## 🚀 Getting Started

Follow these steps to play the game:

1. **Clone the repository**
```bash
git clone https://github.com/sudinkatuwal7/ping-pong.git
```
2. **Navigate to the project folder**
```
cd ping-pong
```
3. **Run the game**
```
python main.py
```
4. Control the paddles

**Left Player:**

w → Move Up

s → Move Down

**Right Player:**

Up Arrow → Move Up

Down Arrow → Move Down

---
## 📂 File Structure
```
ping-pong/ 🏓
│
├── main.py          # Main game loop and screen setup
├── paddle.py        # Paddle class and movement logic
├── ball.py          # Ball movement, collision, and speed control
├── scoreboard.py    # Score tracking and display
└── README.md        # Project documentation
```
## 🧩 Code Structure

- **main.py**
  - Sets up the screen and runs the game loop
  - Handles keyboard inputs
  - Detects collisions and updates scores

- **paddle.py**
  - `Paddle` class for player paddles
  - Movement methods: `go_up()` and `go_down()`

- **ball.py**
  - `Ball` class for ball behavior
  - Methods: `move()`, `x_bounce()`, `y_bounce()`, `restart_ball()`

- **scoreboard.py**
  - `Scoreboard` class to track scores
  - Methods: `l_point()`, `r_point()`, `update_scoreboard()`

---

## 🎨 Tech Stack

- Python 3.7 🐍
- Turtle Graphics (built-in module) 🎨
- Object-Oriented Programming (Classes & Methods) 💻

---

## 🌟 Future Enhancements

- Add sound effects 🔊
- Single-player mode with AI paddle 🤖
- Increase ball speed over time ⚡
- Winning score & game-over screen 🏆
- Add start menu, pause, and game-over screens 🛑

---

## 💡 Tips & Tricks

- Play with a friend for maximum fun! 👫
- Experiment with paddle speed or ball speed in `paddle.py` and `ball.py`
- Modify the scoreboard font or colors to make it your own 🎨

---

## 📸 Screenshots

<img width="1499" height="1245" alt="Screenshot (164)" src="https://github.com/user-attachments/assets/3d7fcfa7-4578-49ea-b1fb-354af14d926e" />



# 🏓 Python Ping Pong Game

A classic **Ping Pong game** built in **Python** using **Turtle graphics** and **Object-Oriented Programming (OOP)** principles.  
Play a fun, interactive game while exploring clean, modular Python code! 🎮🐍

---

## ✨ Features

- **Two-player gameplay** on the same keyboard
- **Ball mechanics**
  - Bounces off paddles
  - Bounces off walls
  - Resets when a player misses
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
git clone https://github.com/yourusername/python-ping-pong.git
```
2. **Navigate to the project folder**
```
cd python-ping-pong
```
3. **Run the game**
```
python main.py
```
4. Control the paddles

**Left Player:**

W → Move Up

S → Move Down

**Right Player:**

Up Arrow → Move Up

Down Arrow → Move Down

---
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
- Add start menu, pause, and game-over screens 🛑

---

## 💡 Tips & Tricks

- Play with a friend for maximum fun! 👫
- Experiment with paddle speed or ball speed in `paddle.py` and `ball.py`
- Modify the scoreboard font or colors to make it your own 🎨

---

## 📸 Screenshots

*(You can add images here if you want to showcase the game)*


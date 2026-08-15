# 🏃 Modi Runner

A fun 2D endless runner game built with Python and Pygame Community Edition (`pygame-ce`). Play as **Modi**, jump over obstacles, dodge flying enemies, and aim for the highest score!

---

## 🎭 Characters & Enemies

- **Player (Modi)**: The running protagonist with custom walk and jump animations.
- **Ground Obstacle (Rahul Gandhi)**: Slides along the ground as the snail obstacle.
- **Air Obstacle (Trump)**: Flies across the screen at mid-air height as the flying enemy.

---

## ✨ Features

- **Custom Character Animations**: Multi-frame running and jumping animations for Modi, plus animated enemy sprites.
- **Dynamic Obstacles**: Randomized spawns for ground enemies (Rahul Gandhi snail) and flying hazards (Trump fly).
- **Parallax Background**: Multi-layered scrolling background with sky and ground elements.
- **Sound Effects & Music**: Background soundtrack, jump audio, and game-over sound effects.
- **Score System**: Live in-game score tracking with a game-over summary screen.
- **Interactive Controls**: Supports keyboard (Space) and mouse-click jump triggers.

---

## 🛠️ Requirements

- Python 3.x
- [Pygame-CE](https://pyga.me/) (`pygame-ce`)

Install dependencies with:

```bash
pip install pygame-ce
```

*(or `pip install -r requirements.txt`)*

---

## 🚀 Getting Started

1. **Navigate to the game directory**:
   ```bash
   cd modi_runner
   ```

2. **Run the game**:
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

- **Spacebar / Left Click**: Start the game / Jump over obstacles
- **Goal**: Dodge incoming obstacles (Rahul Gandhi & Trump) for as long as possible to increase your score
- **Game Over**: Colliding with any obstacle ends the run and displays your final score. Press **SPACE** to restart!

---

## 📁 File Structure

```
modi_runner/
├── assets/
│   ├── characters/      # Modi player, Rahul Gandhi (snail), and Trump (fly) frames
│   ├── environment/     # Parallax background graphics (sky & road)
│   └── intro/           # Splash screen & standing character assets
├── audio/               # Background music, jump sound, and game over FX
├── font/                # PixeloidSans font
├── main.py              # Main game loop and sprite logic
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 👨‍💻 Author

Created by [@Ishant25Dubey](https://x.com/Ishant25Dubey)

---

## 📄 License

This project is open source and available for learning purposes.

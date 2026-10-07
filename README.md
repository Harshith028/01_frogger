# Frogger Lab

## 1. Game Introduction

This is a **Pygame-based Frogger game** created for the Vibe Coding lab.

The lab focuses on understanding an existing game, debugging issues, and adding new functionality using AI-assisted development while critically reviewing and testing AI-generated code.

---

## 2. What Is Provided

The starter project includes:

- A playable frog controlled using the arrow keys
- Moving vehicles across multiple road lanes
- A goal zone and starting zone
- Basic game rendering and game loop
- Restart functionality using `R`
- One existing bug
- Basic functionality required for the remaining features

Use an LLM such as ChatGPT or Claude as a debugging and pair-programming assistant. You are responsible for reviewing, testing, and validating any generated code.

---

## 3. Tasks

### Task 1 — Fix Vehicle Collision Detection

Fix the existing vehicle collision behaviour so that collisions are detected correctly.

### Task 2 — Implement Lives and Respawn

Add a 3-life system with appropriate frog respawn behaviour after a collision.

### Task 3 — Implement Goal and Score Tracking

Detect successful goal completion and implement score tracking with an appropriate win state.

### Task 4 — Add a 30-Second Timer

Add a 30-second countdown for each attempt and handle timeout appropriately.

---

## 4. Expected Behaviour

- The frog moves correctly using the arrow keys.
- Vehicle collisions are detected reliably.
- The player has 3 lives.
- The frog respawns appropriately after losing a life.
- Reaching the goal results in a win.
- The current score is displayed during gameplay.
- Each attempt has a 30-second time limit.
- Running out of time has an appropriate effect on the current attempt.
- Losing all lives results in Game Over.
- Pressing `R` restarts the game.

---

## 5. Submission Checklist

- [ ] All 4 tasks are completed.
- [ ] The game runs without errors.
- [ ] A 10-second video of the game before your changes, showing the original bug/broken behaviour.
- [ ] A 10-second video of the game after your changes, showing the completed functionality.
- [ ] Link to the Chat/LLM page containing the complete chat history used during development.

---

## 6. Project Structure

```text
frogger/
├── README.md
├── requirements.txt
├── main.py
└── game/
    ├── __init__.py
    ├── game_engine.py
    ├── frog.py
    ├── vehicle.py
    ├── collisions.py
    └── renderer.py

## Completed Tasks

### Task 1 – Vehicle Collision Detection
- Implemented reliable collision detection using Pygame rectangle overlap.
- The frog loses a life when it overlaps with a vehicle.

### Task 2 – Lives and Respawn
- Added 3 lives for each game.
- After a collision, the frog respawns at the starting position.
- When all 3 lives are lost, the game displays Game Over.
- Press `R` to restart the game.

### Task 3 – Goal, Score and Win State
- Added a goal row at the top of the game.
- Reaching the goal awards 100 points.
- The game displays a `YOU WIN!` state.
- Press `R` to restart after winning.

### Task 4 – 30-Second Countdown
- Added a 30-second countdown for every attempt.
- When the timer reaches zero, the current attempt is lost.
- The frog respawns and the timer resets to 30 seconds.
- If all lives are lost, the game ends.

## Controls

| Key | Action |
|---|---|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| R | Restart |

## Testing

The completed game was tested for:

- Vehicle collision
- Life reduction
- Frog respawn
- Game Over
- 30-second timeout
- Goal detection
- Score tracking
- Win state
- Game restart

Before and after demonstration videos were also recorded.
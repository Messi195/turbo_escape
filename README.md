# Dodge the Obstacles

## Description

**Dodge the Obstacles** is a simple 2D arcade game where the player controls a car and needs to avoid colliding with randomly moving obstacles. The goal is to navigate the car around the screen while dodging the incoming obstacles.

The car can move in all directions, and obstacles randomly change their direction. A collision with an obstacle ends the game.

## Features

- Smooth car movement with diagonal control.
- Randomly moving obstacles that change direction.
- Collision detection with game over state.
- Rotating car to give a dynamic feel while moving in different directions.
- Simple and intuitive controls.

## How to Play

1. **Arrow Keys**: Use the arrow keys to move the car in all directions. You can also move diagonally by pressing two keys at once.
2. **Goal**: Avoid colliding with the obstacles that randomly move around the screen.
3. **End Condition**: The game ends when the car collides with any of the obstacles.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/dodge-the-obstacles.git
    ```

2. Navigate to the project folder and install the required dependencies:

    ```bash
    cd dodge-the-obstacles
    pip install pygame
    ```

3. Download or create the following image files and place them in the project folder:
    - `bg.png` – Background image for the game.
    - `fl.png` – Image of the car (should be a small transparent PNG).
    - `en.png` – Image of the obstacle (should also be a small transparent PNG).

4. Run the game:

    ```bash
    python game.py
    ```

## Controls

- **Arrow Keys**: Move the car in all directions.
  - **Up**: Move up.
  - **Down**: Move down.
  - **Left**: Move left.
  - **Right**: Move right.
  - **Diagonal Movement**: Hold two keys simultaneously to move diagonally.

## Dependencies

- Python 3.x
- Pygame

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


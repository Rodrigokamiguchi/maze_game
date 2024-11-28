## Introduction
This maze game is developed in Python using the Pygame library, leveraging object-oriented programming (OOP) principles for modularity and scalability. The game challenges players to navigate increasingly complex mazes, overcome obstacles such as monsters and locked doors, and strategically use keys to progress. The scoring system rewards players based on their completion speed, promoting replayability and skill improvement.

## Features
Levels:

20 predefined levels with increasing complexity.
Monsters, doors, and keys are introduced starting from level 10.
Procedural generation for maze layouts ensures variety in design.
Game Elements:

Monsters: Represented as pink dots, they move randomly and cause the game to end upon collision.
Doors: Represented as golden dots, they block the player’s path and require keys to unlock.
Keys: Represented as yellow dots, each key corresponds to one door.
Scoring System:

Based on the speed at which the player completes each level.
Faster completion results in higher scores, encouraging efficiency.
Power-ups:

Speed boosts (optional feature) are scattered in some levels to enhance player movement temporarily.
Messages:

Real-time display messages for events such as picking up keys, unlocking doors, or colliding with monsters.
## Gameplay
Objective: Navigate the maze from the starting point to the finish line while avoiding monsters and unlocking doors using keys.
Rules:
Avoid monsters; collision results in "Game Over."
Collect keys to unlock doors and progress.
Complete the level within the shortest time possible to maximize the score.
Progression:
Levels 1-9: Simple maze navigation.
Levels 10-20: Introduction of monsters, doors, and keys for added complexity.
## Technical Details
Programming Language: Python

Library: Pygame

Game Architecture:

Object-Oriented Design with classes for Player, Monster, Door, Key, and Maze.
Event-driven game loop handling user inputs, collisions, and level progression.
Key Classes:

Player: Manages movement, collision detection, and interaction with game elements.
Monster: Implements random movement logic and collision behavior.
Maze: Generates and renders maze layout dynamically for each level.
Door and Key: Handle placement and unlocking mechanics.
Graphics:

Simple 2D sprites for game elements.
Color-coded representation for easy differentiation:
Pink: Monsters
Yellow: Keys
Golden: Doors
Sound and Animations:

Optional feature: Background music and sound effects for interactions (e.g., picking up a key, unlocking a door).
Explosion animation upon collision with a monster.
## Installation and Setup
Dependencies:

Python 3.10 or later
Pygame library (pip install pygame)
Running the Game:

Clone the repository or download the game files.
Run the main script:
bash
Copiar código
python maze_game.py
Configuration:

Difficulty settings can be adjusted by modifying the speed of monsters or the complexity of the maze in the code.
Game levels are easily expandable by adding new maze layouts.
## Future Enhancements
Procedural generation of maze layouts for infinite levels.
Online leaderboard to track player scores.
Multiplayer mode for cooperative or competitive gameplay.
Additional power-ups, such as invisibility to bypass monsters.
## Acknowledgments
This game was developed as a project to explore Python’s capabilities in game development. It combines problem-solving mechanics with engaging gameplay to provide an enjoyable experience for players of all ages.

## Image

![image](https://github.com/user-attachments/assets/c374cf3a-b09d-4a09-94b9-d1d9ccd58057)
![image](https://github.com/user-attachments/assets/766b12ed-a88f-4cc5-ae81-08577f9c6acf)





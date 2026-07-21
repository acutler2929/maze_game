# maze_game

## Game Name : Mouse Maze Escape

# Game Idea

Our game is a simple 2D maze game. The player controls a small mouse that is trying to escape from a maze. There are many different paths inside the maze, but only one path leads to the correct exit. While exploring, the mouse can collect pieces of cheese to earn points.

The maze also has traps and cats. If the mouse steps on a trap, the game restarts from the beginning. The cats are enemies that move around the maze. If a cat catches the mouse, the player also loses and must restart the game.

The player must collect cheese, avoid the cats and traps, and find the correct way out of the maze.


# Story

A little mouse is trapped inside a big maze. The mouse is looking for cheese while trying to find the only safe way out. Cats are walking around the maze looking for the mouse, and traps are hidden in different places. The player must be careful and choose the correct path to escape.


# Game Objective

* Help the mouse escape the maze.
* Collect cheese to earn points.
* Avoid the cats.
* Do not step on traps.
* Find the only correct exit.


# Game Features

* 2D top-down maze
* Mouse as the player
* Cats as enemies
* Cheese to collect
* Traps that restart the game
* Score system
* Win screen
* Game over screen
* Multiple paths
* Only one correct path to the exit

# What We Need

## Player

* Mouse character
* Movement using WASD or Arrow Keys
* Walking animation

## Enemies

* Cat characters
* Cats move around the maze
* Cats chase or patrol the maze

## Maze

* Walls
* Different paths
* Start point
* Exit point
* Dead ends

## Items

* Cheese
* Traps

## User Interface

* Score
* Cheese collected
* Restart message
* Win message

## Sounds

* Cheese collection sound
* Trap sound
* Cat sound (optional)
* Win sound
* Background music (optional)
  
# How We Will Make the Game

First, we will build the maze using walls and paths. Then we will place the mouse at the starting point. After that, we will place cheese, traps, and cats around the maze.

The player will move the mouse using the keyboard. When the mouse touches a piece of cheese, the cheese disappears and the score increases. If the mouse steps on a trap, the game restarts. If a cat catches the mouse, the player loses and the game restarts.

Only one path in the maze leads to the exit. The player must explore carefully and remember the correct path.


# Programming Concepts

We will use these programming concepts:

* Variables to store the score, player position, lives, and cheese collected.
* If statements to check if the mouse touches cheese, a trap, a cat, or the exit.
* Loops to keep the game running.
* Functions to move the player, move the cats, restart the game, and check collisions.
* Collision detection to know when the mouse touches walls, cheese, traps, cats, or the exit.
* Arrays or lists to save the locations of cheese, traps, walls, and cats.
* Simple enemy AI so the cats can move around the maze or patrol between paths.

# Game Strategy

The player must think carefully before choosing a path. Some paths have more cheese, but they may also have traps or cats. Only one path leads to the exit. The player should remember where they have already explored and avoid dangerous areas. Collecting more cheese gives a higher score, but it also increases the risk of getting caught.


# Winning

The player wins when the mouse reaches the correct exit without getting caught by a cat or stepping on a trap.


# Losing

The player loses if:

* The mouse steps on a trap.
* A cat catches the mouse.

When the player loses, the game restarts from the beginning.


# Future Ideas

If we have more time, we can add:

* More maze levels
* Bigger mazes
* Faster cats
* Countdown timer
* Hidden cheese
* Speed boost power-ups
* Different difficulty levels
* High score leaderboard
* More than one cat chasing the player

# Summary

Our game is a simple and fun 2D maze game. The player controls a mouse that explores a maze, collects cheese, avoids cats and traps, and tries to find the only correct way out. The game uses beginner programming concepts such as variables, loops, functions, collision detection, arrays, and simple enemy movement. It is easy to understand but still gives the player a fun challenge.

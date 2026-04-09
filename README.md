# DungeonCrawler

## Repository
<Link to your project's public GitHub respository>

## Description
A 2d pixel dungeon crawler game that allows players to explore and fight a randomized dungeon. It will be turn-based and text-heavy with elements of dice rolling and equipment power-ups.

## Features
- Randomized map
	- To create a sense of randomness in every game, the map has to be different. I would need to create an algorithm that picks from a list of random rooms, which will be categorized based on treasure, enemy, or nothing. The size of the map will be hard set to a grid size I have not thought of yet. 
- Dice based combat system
	- Creating the dice roll should be simple to make with the randomize function. The output of the roll should be contested with enemy rolls which can be setup using an if, else statement function and player setup encounters.
- Powerup system 
	- The player starts off with a basic stat block that they can upgrade through out the dungeon. Encountering a treasure room and finding powerups will add onto their stats, returning a modified stat block.

## Challenges
- I would need to study more on arrays and how to randomize categorized rooms so it's balanced.
- Movement system using "WASD", and how to create encounter screens that you can interact with.
- I need to research more about win and loss logic.

## Outcomes
Ideal Outcome:
- A game where the player can navigate a randomized dungeon and encounter treasures that power-up stat blocks, which can be used against enemies.

Minimal Viable Outcome:
- A game where the player can navigate a simple dungeon, random or not, and power-up stat blocks.

## Milestones

- Week 1
  1. Create code for categorized rooms. Enemy encounter, treasure encounter, or nothing.
  2. Create art and visuals for rooms, enemies, and treasure.

- Week 2
  1. Dice-based system
  2. Implement a dice system with contested enemy encounters

- Week N (Final)
  1. Powerup system
  2. Win and loss conditions

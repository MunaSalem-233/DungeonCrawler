import pygame
import random


def main():
    pygame.init()

    # Create a screen size and display for game using pygame import.
    size = 5
    tile = 160
    width = 1024
    height = 1024
    grid_size = size * tile
    ui_height = height - grid_size

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dungeon Crawler")
    font = pygame.font.SysFont("Ariel", 36)

    # Find images and use pygame to load them into game.

    # Map function: Will need to be a randomized grid with enemy and tresure spawns. 

    # Player will have a max hp and start off in a player position on the grid [0, 0].

    # Combat function: Text based combat function. The only choices player has is attack or defend. Enemy and player has a random chance and random dmg output.
    #   Start combat system will randomize enemy stats
    #   Player attack will have a min and max hit chance using if else statements
    #   Enemy attack will have similar min max ratio but they can also dodge.

    # Win condition is killing 5 emenies. Add a "You won!" text.

    #A simple UI display showing player HP, Enemy HP, Messages, Kills.

    # Game loop using if else elif statements to keep the game going after combat is done.
    # Movement using arrow keys and if else elif statements. This will affect player position on the grid if not in combat.
    # Using up, down, and return keys during combat to select choices in combat.

    # Respawn system for enemies and treasure? (maybe)
    # Lose condition if player health goes to 0, display "You died!" text.

    # Player "animation"? Player and enemy sprites flash if they take damage. Use blit and flash surface in images loaded in. 

if __name__ == "__main__":
    main()
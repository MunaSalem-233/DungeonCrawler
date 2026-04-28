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

    x_offset = (width - grid_size) // 2

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dungeon Crawler")
    font = pygame.font.SysFont(None, 36)

    # Find images and use pygame to load them into game.
    player_img = pygame.image.load("player.png")
    enemy_img = pygame.image.load("enemy.png")
    treasure_img = pygame.image.load("treasure.png")
    floor_img = pygame.image.load("floor.jpg")

    # Player will have a max hp and start off in a player position on the grid [0, 0].
    player_pos = [0, 0]
    player_hp = 100
    player_max = 100
    treasure = 0
    kills = 0

    # Map function: Will need to be a randomized grid with enemy and tresure spawns. 
    def random_pos(exclude):
        while True:
            pos = [random.randint(0, size-1), random.randint(0, size-1)]
            if pos not in exclude:
                return pos
            
    def spawn():
        enemies = [random_pos([player_pos]) for _ in range(5)]
        treasures = [random_pos([player_pos] + enemies) for _ in range(3)]
        return enemies, treasures
    
    enemies, treasures = spawn()

    def draw_bar(x, y, w, h, value, max_val):
        ratio = value / max_val
        pygame.draw.rect(screen, (255,0,0), (x,y,w,h))
        pygame.draw.rect(screen, (0,255,0), (x,y,w*ratio,h))

    def draw():
        screen.fill((0,0,0))

        screen.blit(pygame.transform.scale(floor_img, (width, height)), (0, 0))

        screen.blit(player_img) 
                     

        if player_pos in enemies:
            screen.blit(pygame.transform.scale(enemy_img, ()),
                        (width//2 - 150, height//2 - 150))
        elif player_pos in treasures:
            screen.blit(pygame.transform.sclae(treasure_img, ()),
                        (width//2 - 100, height//2 - 100))


    # Combat function: Text based combat function. The only choices player has is attack or defend. Enemy and player has a random chance and random dmg output.
    #   Start combat system will randomize enemy stats
    #   Player attack will have a min and max hit chance using if else statements
    #   Enemy attack will have similar min max ratio but they can also dodge.

    # Win condition is killing 5 emenies. Add a "You won!" text.

    #A simple UI display showing player HP, Enemy HP, Messages, Kills.

    # Game loop using if else elif statements to keep the game going after combat is done.
    # Movement using arrow keys and if else elif statements. This will affect player position on the grid if not in combat.
    # Using up, down, and return keys during combat to select choices in combat.
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()
        pygame.display.flip()

    # Respawn system for enemies and treasure? (maybe)
    # Lose condition if player health goes to 0, display "You died!" text.

    # Player "animation"? Player and enemy sprites flash if they take damage. Use blit and flash surface in images loaded in. 

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random


def main():
    pygame.init()

    # Create a screen size and display for game using pygame import.
    size = 5
    width = 1024
    height = 1024

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dungeon Crawler")
    clock = pygame.time.Clock()
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

    state = "explore"
    message = "Explore the dungeon..."

    options = ["Attack", "Defend"]
    selected = 0

    enemy_hp = 0
    enemy_max = 0

    flash_timer = 0
    bob_timer = 0
    bob_offset = 0

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

    def start_combat():
        nonlocal state
        nonlocal enemy_hp
        nonlocal enemy_max
        nonlocal message

        state = "combat"

        enemy_max = random.randint(40, 70)
        enemy_hp = enemy_max

        message = "An enemy appears!"

    def player_attack():
        nonlocal enemy_hp
        nonlocal message

        hit_chance = min(0.7 + treasure * 0.05, 0.95)

        if random.ransom() < hit_chance:
            dmg = random.randint(10, 20)
            enemy_hp -= dmg

            message = f"You hit for {dmg}!"
        else:
            message = "You missed!"

    def enemy_turn(defending):
        nonlocal player_hp
        nonlocal message

        dodge = 0.2 + (0.3 if defending else 0)

        if random.random() < dodge:
            message = "You dodged!"
            return
        
        dmg = random.randint(5, 15)
        player_hp -= dmg

        message = f"Enemy hits for {dmg}!"
        
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
            
        if flash_timer > 0:
            flash = pygame.Surface((width, height))
            flash.fill((255, 255, 255))
            flash.set_alpha(150)
            screen.blit(flash, (0, 0))


    # Combat function: Text based combat function. The only choices player has is attack or defend. Enemy and player has a random chance and random dmg output.
    #   Start combat system will randomize enemy stats
    #   Player attack will have a min and max hit chance using if else statements
    #   Enemy attack will have similar min max ratio but they can also dodge.

    # Win condition is killing 5 emenies. Add a "You won!" text.

    #A simple UI display showing player HP, Enemy HP, Messages, Kills.

    # Game loop using if else elif statements to keep the game going after combat is done.
    # Movement using arrow keys and if else elif statements. This will affect player position on the grid if not in combat.
    # Using up, down, and return keys during combat to select choices in combat.
    running = True

    while running:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                moved = False

                if event.key == pygame.K_UP and player_pos[0] > 0:
                    player_pos[0] -= 1
                    moved = True
                elif event.key == pygame.K_DOWN and player_pos[0] < size-1:
                    player_pos[0] += 1
                    moved = True
                elif event.key == pygame.K_LEFT and player_pos[1] > 0:
                    player_pos[1] -= 1
                    moved = True
                elif event.key == pygame.K_RIGHT and player_pos[1] < size-1:
                    player_pos[1] += 1
                    moved = True

                if moved:
                    flash_timer = 3

                    if player_pos in enemies:
                        enemies.remove(player_pos)
                        enemies.remove(player_pos)
                        kills += 1
                        print(f"Enemy defeated! ({kills}/10)")

                    elif player_pos in treasures:
                        treasures.remove(player_pos)
                        treasure += 1
                        print("Found treasure!")

        if flash_timer > 0:
            flash_timer -= 1


        draw()
        pygame.display.flip()

    # Respawn system for enemies and treasure? (maybe)
    # Lose condition if player health goes to 0, display "You died!" text.

    # Player "animation"? Player and enemy sprites flash if they take damage. Use blit and flash surface in images loaded in. 

    pygame.quit()

if __name__ == "__main__":
    main()
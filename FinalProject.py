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
    big_font = pygame.font.SysFont(None, 72)

    # Find images and use pygame to load them into game.
    player_img = pygame.image.load("player.png")
    enemy_img = pygame.image.load("enemy.png")
    treasure_img = pygame.image.load("treasure.png")
    floor_img = pygame.image.load("floor.jpg")

    # Player will have a max hp and start off in a player position on the grid [0, 0].
    player_pos = [2, 2]
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
    treasure_timer = 0

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

        if random.random() < hit_chance:
            dmg = random.randint(10, 20)
            enemy_hp -= dmg
            enemy_hp = max(enemy_hp, 0)

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
        player_hp = max(player_hp, 0)

        message = f"Enemy hits for {dmg}!"

    def draw_bar(x, y, w, h, value, max_val):
        ratio = value / max_val

        pygame.draw.rect(screen, (120, 0, 0), (x, y, w, h))
        pygame.draw.rect(screen, (0, 200, 0), (x, y, w * ratio, h))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h), 2)

    def draw():
        screen.fill((0,0,0))

        screen.blit(pygame.transform.scale(floor_img, (width, height)), (0, 0))

        if state != "dead":
            screen.blit(
                player_img,
                (
                    width // 2 - player_img.get_width() // 2,
                    height // 2 - player_img.get_height() // 2 + bob_offset
                )
            )

                     

        if state == "combat":
            screen.blit(enemy_img,(width//2 - 150, height//2 - 150))
        elif player_pos in treasures:
            screen.blit(treasure_img, (width//2 - 100, height//2 - 100))

            
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
        pygame.draw.rect(
            screen,
            (20, 20, 20),
            (0, height - 220, width, 220)
        )

        # Message UI
        msg = font.render(message, True, (255, 255, 255))
        screen.blit(msg, (40, height - 190))
        
        # HP bar UI
        draw_bar(40, height - 140, 300, 25, player_hp, player_max)

        player_text = font.render(
            f"Player HP: {player_hp}/{player_max}",
            True,
            (255, 255, 255)
        )
        screen.blit(player_text, (40, height - 170))

        if state == "combat":
            draw_bar(
                width - 340,
                height - 140,
                300,
                25,
                enemy_hp,
                enemy_max
            )

            enemy_text = font.render(
                f"Enemy HP: {enemy_hp}/{enemy_max}",
                True,
                (255, 255, 255)
            )

            screen.blit(enemy_text, (width - 340, height - 170))

        # Combat Options
        if state == "combat":
            for i, opt in enumerate(options):
                color = (
                    (255, 255, 0)
                    if i == selected
                    else (200, 200, 200)
                )

                text = font.render(opt, True, color)

                screen.blit(
                    text,
                    (60, height - 90 + i * 40)
                )

        # Stats
        stats = font.render(
            f"Treasures: {treasure}  Kills: {kills}/10",
            True,
            (255, 255, 255)
        )

        screen.blit(stats, (500, height - 90))

        # Dead screen
        if state == "dead":

            overlay = pygame.Surface((width, height))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))

            screen.blit(overlay, (0, 0))

            dead_text = big_font.render(
                "You have perished :(",
                True,
                (255, 0, 0)
            )

            screen.blit(
                dead_text,
                (
                    width // 2 - dead_text.get_width() // 2,
                    height // 2 - 100
                )
            )

            restart_text = font.render(
                "Pres ESC to quit",
                True,
                (255, 255, 255)
            )

            screen.blit(
                restart_text,
                (
                    width // 2 - restart_text.get_width() // 2,
                    height // 2
                )
            )
        
        # Win Screen
        if state == "win":

            overlay = pygame.Surface((width, height))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))

            screen.blit(overlay, (0, 0))

            win_text = big_font.render(
                "You beat the dungeon!",
                True,
                (255, 0, 0)
            )

            screen.blit(
                win_text,
                (
                    width // 2 - win_text.get_width() // 2,
                    height // 2 - 100
                )
            )

            quit_text = font.render(
                "Press ESC to quit",
                True,
                (255, 255, 255)
            )

            screen.blit(
                quit_text,
                (
                    width // 2 - quit_text.get_width() // 2,
                    height // 2
                )
            )

        pygame.display.flip()



    # Game loop using if else elif statements to keep the game going after combat is done.
    # Movement using arrow keys and if else elif statements. This will affect player position on the grid if not in combat.
    # Using up, down, and return keys during combat to select choices in combat.
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if state in ["dead", 'win']:

                    if event.key  == pygame.K_ESCAPE:
                        running = False

                elif state == "explore":
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
                        flash_timer = 4
                        bob_timer = 24

                        if player_pos in enemies:
                            enemies.remove(player_pos)
                            start_combat()

                        elif player_pos in treasures:
                            treasures.remove(player_pos)
                            treasure += 1
                            treasure_timer = 30
                            if random.random() < 0.6:
                                heal = random.randint(10, 25)
                                player_hp += heal
                                player_hp = min(player_hp, player_max)

                                message = f"Found treasure! Healed for {heal} HP."
                            else:
                                message = ("Found treasure!")

                elif state == "combat":

                    if event.key == pygame.K_UP:
                        selected = (selected -1) % len(options)

                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)

                    elif event.key == pygame.K_RETURN:

                        if options[selected] == "Attack":

                            player_attack()

                            if enemy_hp <= 0:
                                kills += 1

                                message = "Enemy defeated!"
                                state = "explore"

                                if kills >= 10:
                                    message = "You beat the dungeon!"
                                    running = False

                            else:
                                enemy_turn(False)

                        elif options[selected] == "Defend":

                            message = "You brace for impact!"
                            enemy_turn(True)

        
        # Animation
        if flash_timer > 0:
            flash_timer -= 1
        if bob_timer > 0:
            bob_timer -= 1

            if bob_timer > 18:
                bob_offset = -3
            elif bob_timer > 12:
                bob_offset = 0
            elif bob_timer > 6:
                bob_offset = 3
            else:
                bob_offset = 0

        else:
            bob_offset = 0

        if treasure_timer > 0:
            treasure_timer -= 1

        if player_hp <= 0:
            player_hp = 0
            state = "dead"
            message = "You have perished :("


        draw()
        pygame.display.flip()

    # Respawn system for enemies and treasure? (maybe)
    # Lose condition if player health goes to 0, display "You died!" text.

    # Player "animation"? Player and enemy sprites flash if they take damage. Use blit and flash surface in images loaded in. 

    pygame.quit()

if __name__ == "__main__":
    main()
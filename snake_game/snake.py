import pygame
import time
import random

# initialize the game
pygame.init()

# Define collor to use on Snake , screen and food
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (50, 153, 213)
yellow = (255, 255, 102)
green = (0, 255, 0)

# Define the screen size
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

# Define the game name
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake_block = 10
while True:
    try:
        level_speed = int(input("Choose the level: 1-Beginner, 2-Medium, 3-Hard "))
        if level_speed == 1:
            snake_speed = 15
        elif level_speed == 2:
            snake_speed = 20
        elif level_speed == 3:
            snake_speed = 30
        else:
            print("Invalid option!!")
    except:
        continue
    else:
        break

font_style = pygame.font.SysFont("bahnschrift", 50)
score_font = pygame.font.SysFont("comicsansms", 50)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


def our_snake(snake_block_, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block_, snake_block_])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = list()
    length_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    # Guarantee the screen still open while the game doesn't finish or bottom close is clicked
    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You lose! Press Q-Quit or C-Play Again", red)
            your_score(length_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    game_loop()

        for event in pygame.event.get():
            # Quit the screen when hit the close bottom
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or x1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        # Change the screen collor from black to white
        dis.fill(blue)

        # Draw the snake, a rectangle
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = list()
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_snake - 1)

        # Draw the snake, a rectangle
        #pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

        # Update the screen
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    # Quit the game
    pygame.quit()
    quit()

game_loop()

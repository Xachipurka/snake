import random
import pygame
import time

from snake import Snake


pygame.init()
#
screen = pygame.display.set_mode((470, 500))

running = True

snake = Snake('green', [[3, 3], [2, 3], [1, 3]])
snake2 = Snake('blue', [[1, 3], [1, 2], [1, 1]])

appleX = random.randrange(10)
appleY = random.randrange(10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        snake.update(event, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
        snake2.update(event, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)

    snake.move(appleX, appleY, snake2)
    snake2.move(appleX, appleY, snake)
    headX = snake.position[0][0]
    headY = snake.position[0][1]

    running = snake.running and snake2.running

    if headX == appleX and headY == appleY:
        snake.score += 3
        while True:
            appleX = random.randrange(10)
            appleY = random.randrange(10)
            for i in range(len(snake.position)):
                if appleX == snake.position[i][0] and appleY == snake.position[i][1]:
                    break
            else:
                break

    headX = snake2.position[0][0]
    headY = snake2.position[0][1]

    if headX == appleX and headY == appleY:
        snake.score += 3
        while True:
            appleX = random.randrange(10)
            appleY = random.randrange(10)
            for i in range(len(snake.position)):
                if appleX == snake.position[i][0] and appleY == snake.position[i][1]:
                    break
            else:
                break
    screen.fill((0, 0, 0)) # закрасить экран белым цветом

    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, (0, 255, 255,), (x * 47, y * 47, 45, 45))

    snake.draw(screen)
    snake2.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), (appleX * 47, appleY * 47, 45, 45))

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
    screen.blit(text, (0, 470))

    pygame.display.flip()

pygame.quit()
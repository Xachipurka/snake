import random
import pygame
import time

from snake import Snake


pygame.init()
#
screen = pygame.display.set_mode((470, 500))

running = True

#snake = [[1, 3], [2, 3], [3, 3]] # [[2, 3], [3, 3], [3, 4]]
snake = Snake()

appleX = random.randrange(10)
appleY = random.randrange(10)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        snake.update(event)

    snake.move(appleX, appleY)
    headX = snake.position[0][0]
    headY = snake.position[0][1]

    running = snake.running

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
    pygame.draw.rect(screen, (255, 0, 0), (appleX * 47, appleY * 47, 45, 45))

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {snake.score}', True, (255, 255, 255))
    screen.blit(text, (0, 470))

    pygame.display.flip()

pygame.quit()
import random
import pygame
import time
score = 0
pygame.init()
#
screen = pygame.display.set_mode((470, 500))

running = True

snake = [[1, 3], [2, 3], [3, 3]] # [[2, 3], [3, 3], [3, 4]]

appleX = random.randrange(10)
appleY = random.randrange(10)

time1 = time.perf_counter()
direction = 'UP'

while running:
    headX = snake[0][0]
    headY = snake[0][1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 'UP'
            elif event.key == pygame.K_s:
                direction = 'DOWN'
            elif event.key == pygame.K_d:
                direction = 'RIGHT'
            elif event.key == pygame.K_a:
                direction = 'LEFT'

    time2 = time.perf_counter()
    if time2 - time1 > 0.5:
        if direction == 'UP':
            snake = [[headX,headY - 1]] + snake
        elif direction == 'DOWN':
            snake = [[headX, headY + 1]] + snake
        elif direction == 'RIGHT':
            snake = [[headX + 1, headY]] + snake
        elif direction == 'LEFT':
            snake = [[headX - 1, headY]] + snake
        headX = snake[0][0]
        headY = snake[0][1]
        if appleX != headX or appleY != headY:
            del snake[-1]
        for i in range(1, len(snake)):
            if headX == snake[i][0] and headY == snake[i][1]:
                running = False
        score += 0.5
        time1 += 0.5

    if headX < 0 or headY < 0 or headX > 9 or headY > 9:
        running = False
    if headX == appleX and headY == appleY:
        score += 3
        while True:
            appleX = random.randrange(10)
            appleY = random.randrange(10)
            for i in range(len(snake)):
                if appleX == snake[i][0] and appleY == snake[i][1]:
                    break
            else:
                break

    screen.fill((0, 0, 0)) # закрасить экран белым цветом

    for y in range(10):
        for x in range(10):
            pygame.draw.rect(screen, (0, 255, 255,), (x * 47, y * 47, 45, 45))

    for x, y in snake:
        pygame.draw.rect(screen, (0, 255, 0,), (x * 47, y * 47, 45, 45))
    pygame.draw.rect(screen,  (255, 0, 0), (appleX * 47, appleY * 47, 45, 45))

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (0, 470))


    pygame.display.flip()

pygame.quit()
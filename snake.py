import pygame
from time import perf_counter


class Snake:
    def __init__(self):
        self.position = [[1, 3], [2, 3], [3, 3]]
        self.direction = 'DOWN'
        self.time1 = perf_counter()
        self.score = 0
        self.running = True

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.direction = 'UP'
            elif event.key == pygame.K_s:
                self.direction = 'DOWN'
            elif event.key == pygame.K_d:
                self.direction = 'RIGHT'
            elif event.key == pygame.K_a:
                self.direction = 'LEFT'

    def move(self, appleX, appleY):
        headX = self.position[0][0]
        headY = self.position[0][1]
        time2 = perf_counter()
        if time2 - self.time1 > 0.5:
            if self.direction == 'UP':
                self.position = [[headX, headY - 1]] + self.position
            elif self.direction == 'DOWN':
                self.position = [[headX, headY + 1]] + self.position
            elif self.direction == 'RIGHT':
                self.position = [[headX + 1, headY]] + self.position
            elif self.direction == 'LEFT':
                self.position = [[headX - 1, headY]] + self.position
            headX = self.position[0][0]
            headY = self.position[0][1]
            if appleX != headX or appleY != headY:
                del self.position[-1]
            for i in range(1, len(self.position)):
                if headX == self.position[i][0] and headY == self.position[i][1]:
                    self.running = False
            self.score += 0.5
            self.time1 += 0.5

            if headX < 0 or headY < 0 or headX > 9 or headY > 9:
                self.running = False

    def draw(self, screen):
        for x, y in self.position:
            pygame.draw.rect(screen, (0, 255, 0,), (x * 47, y * 47, 45, 45))

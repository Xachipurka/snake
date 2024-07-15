import pygame
from time import perf_counter


class Snake:
    def __init__(self, color, position):
        self.position = position
        self.direction = 'DOWN'
        self.time1 = perf_counter()
        self.score = 0
        self.running = True
        self.color = color

    def update(self, event, up, right, down, left):
        if event.type == pygame.KEYDOWN:
            if event.key == up:
                self.direction = 'UP'
            elif event.key == down:
                self.direction = 'DOWN'
            elif event.key == right:
                self.direction = 'RIGHT'
            elif event.key == left:
                self.direction = 'LEFT'

    def move(self, appleX, appleY, snake2):
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

            for i in range(len(snake2.position)):
                if headX == snake2.position[i][0] and headY == snake2.position[i][1]:
                    self.running = False

            self.score += 0.5
            self.time1 += 0.5

            if headX < 0 or headY < 0 or headX > 9 or headY > 9:
                self.running = False

    def draw(self, screen):
        for x, y in self.position:
            pygame.draw.rect(screen, self.color, (x * 47, y * 47, 45, 45))

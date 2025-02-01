import pygame
import random

class Ball:

    def __init__(self, X, Y, R):
        self.posX = X
        self.posY = Y
        self.radius = R 
        self.speedX = 0
        self.speedY = 0
    
    def setRandomSpeed(self):
        self.speedX = 1 + 4#random.randint(-4,4)
        self.speedY = 1 + 4#random.randint(-4,4)

    def update(self):
        self.posX += self.speedX
        self.posY += self.speedY
    
    def render(self,screen):
        pygame.draw.circle(screen, pygame.Color("white"),
                           (self.posX, self.posY), self.radius)
import pygame
from ball import Ball

class Paddle:

    def __init__(self, X, Y):
        self.posX = X
        self.posY = Y
        self.height = 100
        self.width = 10

    def moveUp(self):
        self.posY -= 9

    def moveDown(self):
        self.posY += 9
    
    def collides(self, ball):
        return ball.posX >= self.posX and ball.posX <= self.posX + self.width and \
               ball.posY >= self.posY and ball.posY <= self.posY + self.height
    
    def render(self,screen):
        pygame.draw.line(screen, pygame.Color("red"), [self.posX, self.posY],
                         [self.posX, self.posY+self.height], self.width)
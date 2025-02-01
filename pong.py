import pygame
from ball import Ball
from paddle import Paddle

BLACK = (0,0,0)
WHITE = (255,255,255)

class PingPongGame:
    def __init__(self):
        pygame.init()
        self.screenSize = (700, 500)
        self.running = False

    def start(self):
        self.init()
        self.run() 
    
    def init(self):
        self.running = True
        # Init screen window
        self.screen = pygame.display.set_mode(self.screenSize)
        # Add caption to the window
        pygame.display.set_caption("Ping Pong")
        # Init clock for fps
        self.clock = pygame.time.Clock()
        
        # Init objects
        self.ball = Ball(350,250,10)
        self.ball.setRandomSpeed()
        self.rpaddle = Paddle(10,240)
        self.lpaddle = Paddle(685,240)

    def end(self):
        pygame.quit()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.render()
        self.end()

    def events(self):
        # Retrieve events
        for event in pygame.event.get():
            # QUIT event
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] == True:
            self.lpaddle.moveUp()
        if keys[pygame.K_DOWN]:
            self.lpaddle.moveDown()
        if keys[pygame.K_w]:
            self.rpaddle.moveUp()
        if keys[pygame.K_s]:
            self.rpaddle.moveDown()

    def update(self):
        # Check Collisions
        if self.ball.posY <= 0 or self.ball.posY >= 500:
            self.ball.speedY *= -1
        
        if self.lpaddle.collides(self.ball) or self.rpaddle.collides(self.ball):
            self.ball.speedX *= -1

        if self.ball.posX <= 0 or self.ball.posX >= 700:
            self.running = False

        # Update objects
        self.ball.update()

    def render(self):
        # Clear the screen and draw line
        self.screen.fill((0,0,0))

        # Render objects
        self.ball.render(self.screen)
        self.lpaddle.render(self.screen)
        self.rpaddle.render(self.screen)

        # Update the screen
        pygame.display.flip()
        # Limit FPS to 60 frame per seconds
        self.clock.tick(60)


if __name__ == "__main__":
    game = PingPongGame()
    game.start()
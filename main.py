import pygame
from constants import *
from player import *

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #initializing screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #initialize clock object
    clock = pygame.time.Clock()
    #clock timer variable
    dt = 0
    #spawn player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        #enabling quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #filling black screen, drawing player and refreshing every loop
        pygame.Surface.fill(screen, (0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()        

        #limiting framerate
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
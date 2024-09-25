import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init
    print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    #initializing screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #initialize clock object
    clock = pygame.time.Clock()
    #clock timer variable
    dt = 0

    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #add objects to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    #spawn sprites
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidFieldSprites = AsteroidField()
    

    while True:
        #enabling quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)
        #filling black screen, drawing player and refreshing every loop
        pygame.Surface.fill(screen, (0,0,0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()        

        #limiting framerate
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
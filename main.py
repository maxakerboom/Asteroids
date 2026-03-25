import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import log_state, log_event

VERSION =  pygame.version.ver



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()
    player_x = Player(x, y, PLAYER_RADIUS)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        for d in drawable:
            d.draw(screen)
        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player_x) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for a in asteroids:
            for s in shots:
                if a.collides_with(s) == True:
                    log_event("asteroid_shot")
                    a.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

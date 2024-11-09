import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)
    
    AsteroidField.containers = (updatable)
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if obj.check_collision(shot):
                    obj.split()
                    shot.kill()
        for obj in shots:
            obj.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

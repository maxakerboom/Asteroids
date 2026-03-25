import pygame
import random
from logger import log_event
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20,50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        a2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
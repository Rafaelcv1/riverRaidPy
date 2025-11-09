import pygame
import Entidade

class Bala(Entidade):
    def __init__(self, sprite ,dims, pos):
        sprite = "sprites/bala.png"
        dims = (4, 4)
        vel = 16
        super().__init__(sprite, dims, pos)
        self.vel = vel

    def movTiro(self):
        while self.y < 804:
            self.y -= self.vel

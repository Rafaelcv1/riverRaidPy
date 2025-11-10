import pygame
import random
from classes.inimigos import Inimigos

class Helic(Inimigos):
    def __init__ (self, pos, velY, direcao):
        sprite = "sprites/helic/helic1.png"
        dims = (32, 32)
        velx = random.randint(3,10)
        super().__init__(sprite, dims, pos, velY, direcao, velx)

def gerarhelic(qnt):
    o = []
    for _ in range(qnt):
        o.append(Helic((random.randint(0, 800-32), -1*random.randint(0,500)), random.randint(2,4), random.randint(0,1)))
    return o



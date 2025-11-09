import pygame
import random
import sys
from classes.aviao import Aviao
from classes.helic import Helic
from classes.helic import gerarhelic
#from classes.gerarHelic import gerarHelic

pygame.init() 
largurat = 800
alturat = 600

gameDisplay = pygame.display.set_mode((largurat, alturat))
pygame.display.set_caption('aviãozinho explode tudo') 
tempo = pygame.time.Clock() 

player = Aviao()

helic_list = gerarhelic(10)

while True:
    gameDisplay.fill("royalblue4")
    tempo.tick(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    tecla = pygame.key.get_pressed()

    player.imprimir(gameDisplay)

    player.movPlayer(tecla)
    for i in helic_list:
        i.imprimir(gameDisplay)
        i.movHoriz()
        i.queda(tecla)

    pygame.display.update()

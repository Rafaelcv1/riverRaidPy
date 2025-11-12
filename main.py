import pygame, random, sys, time
from classes.aviao import Aviao
from classes.helic import *

pygame.init() 
largurat = 800
alturat = 600

gameDisplay = pygame.display.set_mode((largurat, alturat))
pygame.display.set_caption('aviãozinho explode tudo') 
tempo = pygame.time.Clock() 

player = Aviao()

helic_list = []

balas = []
reload_time = 0.25
lastShot = 0

while True:

    for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           sys.exit()

    gameDisplay.fill("royalblue4")
    tempo.tick(30)

    tecla = pygame.key.get_pressed()

    player.imprimir()
    player.movPlayer(tecla)

    #gerar bala
    if tecla[pygame.K_SPACE] and (time.time() - lastShot) >= reload_time:
        balas.append(player.atirar())
        lastShot = time.time()

    if random.randint(0,100) > 1:
        helic_list.append(gerarhelic())
    
    #imprime as entidades em vetores
    for bala in balas:
        bala.imprimir()
        bala.movTiro()
        if bala.y < -32:
            balas.remove(bala)
    
    for helic in helic_list:
        helic.imprimir()
        helic.movHoriz()
        helic.queda(tecla)
        if helic.y < -32:
            helic_list.remove(helic)

    pygame.display.update()

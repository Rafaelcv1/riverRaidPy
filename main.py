import pygame, random, sys, time
from classes.aviao import Aviao
from classes.helic import *
from classes.mapa import *

pygame.init() 
largurat = 800
alturat = 600

gameDisplay = pygame.display.set_mode((largurat, alturat))
pygame.display.set_caption('River Raid Py') 
tempo = pygame.time.Clock() 

player = Aviao()

helics = []

balas = []
reload_time = 0.25
lastShot = 0

map_list = []
first_map = True

col_player = False

while True:

    for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           sys.exit()

    gameDisplay.fill("royalblue4")
    tempo.tick(30)

    tecla = pygame.key.get_pressed()

    #gerar bala
    if tecla[pygame.K_SPACE] and (time.time() - lastShot) >= reload_time:
        balas.append(player.atirar())
        lastShot = time.time()

    #gerar helicopteros
    if random.randint(0,1000) > 330 and len(helics) < 10:
        helics.append(gerarhelic())

    #adiciona 1o modulo a lista de mapas
    if first_map:
        map_list.append(gerarMapa())
        first_map = False

    #for das entidades
    for module in map_list:
        module.imprimir()
        module.queda(tecla)
        
        #apagar modulo que passa da tela
        if module.y > 960:
            map_list.remove(module)

        #gerar modulo
        if module.y > 0 and len(map_list) < 2:
            map_list.append(gerarMapa())
            newMapTime = 0

        #gameOver
        if module.colisaoMask(player):
            col_player = True

    for bala in balas:
        bala.imprimir()
        bala.movTiro()

        #apagar bala fora da tela
        if bala.y < -32:
            balas.remove(bala)
    
    for helic in helics:
        helic.imprimir()
        helic.movHoriz()
        helic.queda(tecla)

        #apagar helicopteros que passaram da tela
        if helic.y > 832:
            helics.remove(helic)

        #gameOver
        if helic.colisaoMask(player):
            col_player = True

        #apagar helicopteros acertador por balas
        for bala in balas:
            helic_hitted = helic.colisaoRect(bala)
            if helic_hitted == True:
                helics.remove(helic)
                balas.remove(bala)

    #gameOver
    if col_player == True:
        sys.exit()

    player.imprimir()
    player.movPlayer(tecla)

    pygame.display.update()

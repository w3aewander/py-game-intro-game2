import time

from PIL import Image
import random

import pygame
import sys
from jogo import \
    controles as ctrl, \
    parametros as parm, \
    graficos as g, \
    colisao as col

from jogo.parametros import *

pygame.mixer.init()
pygame.init()

global som_carro
global size
global width
global height
global linha_pista
global linha
global coluna

screen = pygame.display.set_mode((parm.width,parm.height))

pygame.display.set_caption("Meu primeiro jogo")

carro_path = "img/carro1.png"
carro_player_1 = "img/car_forward.gif"

FORMAT = "RGBA"

carro1 = pygame.image.load(carro_player_1)
carro2 = pygame.image.load(carro_path)
carro3 = pygame.image.load(carro_path)
carro4 = pygame.image.load(carro_path)

clock = pygame.time.Clock()
carr_player_1_gif = Image.open("img/car_forward.gif")
current_frame = 0

#screen.blit(fundo, (0, 0) )
g.indicador_vida(screen, rect=(300, 0, 200, 50), cor=(255,255,255))
g.indicador_vida(screen)

screen.fill((0,0,0))
pygame.display.flip()

coluna_carro2 = 450
linha_carro2 = 200

#clock.tick(25)
frame_carro_player_1 = g.pil_to_game(g.get_gif_frame(carr_player_1_gif, current_frame))

while True:

    linha_carro2 += parm.velocidade

    if linha_carro2 > 650:
        linha_carro2 = - 650
        voltas = voltas + 1


    keys = pygame.key.get_pressed()

    ctrl.ctrl_key(keys)
    screen.fill((0, 0, 0))

    g.desenha_retangulo(screen,cor=(255, 255, 255), rect=((screen.get_width() - 25) / 2, parm.linha_pista, 25, 200))

    frame_carro_player_1 = g.pil_to_game(g.get_gif_frame(carr_player_1_gif, current_frame))
    screen.blit(frame_carro_player_1, (parm.coluna, parm.linha))

    cor_vida = (0, 255, 0)

    if vida <= 0:
        g.escrever_texto(screen, (720, 18), "Você perdeu!")
        pygame.display.update()
        time.sleep(5)
        quit(0)

    if  parm.voltas > 100:
        g.escrever_texto(screen, (720, 18), "Parabéns, você chegou ao final da corrida.")
        pygame.display.update()
        time.sleep(2)
        quit(0)

    if vida <= 50:
        cor_vida = (255, 0, 0)
    elif vida <= 75:
        cor_vida = (255,255,0)
    else:
        cor_vida = (0,255,0)

    g.indicador_vida(screen, cor=cor_vida, rect=(300, 0, vida, 50))

    obj_carro = g.desenha_inimigo(screen, (parm.coluna, parm.linha, frame_carro_player_1.get_width(), frame_carro_player_1.get_width()), cor=(255,0,0))

    objetos = [
        g.desenha_inimigo(screen, rect=(parm.coluna_pista, parm.linha_pista, 100,100),  cor=(255,0,255), filled=0),
        g.desenha_inimigo(screen, rect=(parm.coluna_pista, parm.linha_pista, 100, 100), cor=(0,255,0), filled=0),
        g.desenha_inimigo(screen, rect=(parm.coluna_pista, parm.linha_pista, 100,100 ), cor=(255,255,0), filled=0)
    ]

    if col.colisao(obj_carro, objetos):
        vida = vida - .2

    g.indicador_vida(screen, cor=cor_vida, rect=(300, 0, vida, 50))
    g.escrever_texto(screen, (50,50), f"Volta: {parm.voltas}")

    if parm.linha_pista >= 600:
        parm.coluna_pista = random.randint(100,750)
        parm.linha_pista = 0
        parm.voltas += 1

    parm.linha_pista += 2

    s = "[{0},{1}]".format(parm.coluna, parm.linha)
    g.escrever_texto(screen, (720,18), s)

    pygame.display.flip()



    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
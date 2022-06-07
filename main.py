import random

import pygame
import sys
from jogo import carro


width, height = 800, 600

coluna_pista = 0
linha_pista = 0

pygame.init()

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Meu primeiro jogo")

fundo_path = "img/pista.jpg"
carro_path = "img/carro1.png"

fundo = pygame.image.load(fundo_path)
fundo = pygame.transform.scale(fundo, (800, 600))

carro1 = pygame.image.load(carro_path)
carro2 = pygame.image.load(carro_path)
carro3 = pygame.image.load(carro_path)
carro4 = pygame.image.load(carro_path)

# define a posição do carro na tela.
coluna, linha = 0, 0

screen.blit(fundo, (coluna_pista, linha_pista) )

pygame.display.flip()

# mover a pista para baixo
def mover_fundo(position=(coluna_pista, linha_pista)):
    if position[0] >= 600:
        position[0] = 0

    screen.blit(fundo, position)

def escrever_texto(posicao=(0,0), texto="texto", corTexto=(0,0,0), corFundo=(255,255,255)):
    font = pygame.font.Font('freesansbold.ttf', 22)
    #t = font.render(texto, True, (255,255,220), (0,190,190))
    t = font.render(texto, True, corTexto, corFundo)
    textRect = t.get_rect()
    textRect.center = posicao
    screen.blit(t,textRect)

#mover_fundo((coluna_pista, linha_pista))


def desenha_retangulo():
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(230, 230, 100, 100))

def desenha_circulo(cor=(255,255,255), pos=(10,10)):
    pygame.draw.circle(screen, cor, pos, 100, 50 )


coluna_carro2 = 450
linha_carro2 = 200

while True:

    linha_carro2 -= 1

    if linha_carro2 < -650:
        linha_carro2 = +850

    desenha_retangulo()

    # desenha_circulo(cor=(255,255,0), pos=(550,300))
    # desenha_circulo( pos=(500,400) )
    # desenha_circulo( cor=(0,0,255), pos=(600, 400))

    # for x in range(1):
    #     l = random.randint(100,600)
    #     c = random.randint(100,800)
    #     color_handle_r = random.randint(0, 255)
    #     color_handle_g = random.randint(0, 255)
    #     color_handle_b = random.randint(0, 255)
    #     desenha_circulo(cor=(color_handle_r, color_handle_g, color_handle_b), pos=(c, l))

    s = "[{0},{1}]".format(coluna, linha)
    escrever_texto( (720,18), s)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        coluna -= 1

    if keys[pygame.K_RIGHT]:
        coluna += 1

    if keys[pygame.K_UP]:
        linha -= 1

        #carro_path = "img/carro1.png"
        #carro1.setImage(carro_path)
        screen.blit(carro1, (coluna, linha))

    if keys[pygame.K_DOWN]:
        linha += 1
        #carro_path = "img/seta_baixo.png"
        #carro1.setImage(carro_path)


    #travar o objeto na tela.
    #if coluna < 0: coluna=0
    #if coluna > 765: coluna=765


    if linha > 560: linha = 560

    #if linha < 409: linha= 409
    #if linha < 30: linha = 30


    #linha_pista += 100
    #mover_fundo( position=(coluna_pista, linha_pista))

    mover_fundo(position=(coluna_pista, linha_pista))

    screen.blit(carro1, (coluna, linha))
    screen.blit(carro2, (coluna_carro2, linha_carro2))
    screen.blit(carro3, (coluna_carro2 - 300, linha_carro2 - 150 ))
    screen.blit(carro4, (coluna_carro2 +  100, linha_carro2 + 220 ))

    pygame.display.flip()


    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
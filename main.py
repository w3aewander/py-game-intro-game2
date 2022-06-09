from PIL import Image
import random

import pygame
import sys
from jogo import controles as ctrl

size = width, height = 800, 600

coluna_pista = 0
linha_pista = 0

pygame.init()

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Meu primeiro jogo")

#fundo_path = "img/pista.jpg"
carro_path = "img/carro1.png"
carro_player_1 = "img/car_forward.gif"
FORMAT = "RGBA"

#fundo = pygame.image.load(fundo_path)
#fundo = pygame.transform.scale(fundo, (800, 600))

carro1 = pygame.image.load(carro_player_1)
carro2 = pygame.image.load(carro_path)
carro3 = pygame.image.load(carro_path)
carro4 = pygame.image.load(carro_path)

# define a posição do carro na tela.
coluna, linha = 0, 0

clock = pygame.time.Clock()
carr_player_1_gif = Image.open("img/car_forward.gif")
current_frame = 0

#screen.blit(fundo, (0, 0) )

screen.fill((0,0,0))
pygame.display.flip()

def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)

def init():
    return pygame.display.set_mode(size)


# mover a pista para baixo
def mover_fundo(position=(coluna_pista, linha_pista)):
    if position[0] >= 600:
        position[0] = -10

def escrever_texto(posicao=(0,0), texto="texto", corTexto=(0,0,0), corFundo=(255,255,255)):
    font = pygame.font.Font('freesansbold.ttf', 22)
    #t = font.render(texto, True, (255,255,220), (0,190,190))
    t = font.render(texto, True, corTexto, corFundo)
    textRect = t.get_rect()
    textRect.center = posicao
    screen.blit(t,textRect)

def desenha_retangulo(cor=(255,255,255), rect=(230, 230, 50, 200) ):
    pygame.draw.rect(screen, cor, pygame.Rect(rect))

def desenha_circulo(cor=(255,255,255), pos=(10,10)):
    pygame.draw.circle(screen, cor, pos, 100, 50 )


coluna_carro2 = 450
linha_carro2 = 200

clock.tick(25)
frame_carro_player_1 = pil_to_game(get_gif_frame(carr_player_1_gif, current_frame))

while True:

    linha_carro2 -= 1

    if linha_carro2 < -650:
        linha_carro2 = +850


    s = "[{0},{1}]".format(coluna, linha)
    escrever_texto( (720,18), s)

    keys = pygame.key.get_pressed()

    ctrl.ctrl_key(keys)

    if ctrl.linha > 560: ctrl.linha = 560

    # screen.fill((0, 0, 0), fundo.get_rect())
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen,
                     (random.randint(0,255),
                      random.randint(0,255),
                      random.randint(0,255)), (random.randint(0,800),random.randint(0,600)),1 )
    linha_pista += .9
    if linha_pista > 600: linha_pista = - 250

    desenha_retangulo(cor=(255, 255, 255), rect=((screen.get_width() - 25) / 2, linha_pista, 25, 200))

    frame_carro_player_1 = pil_to_game(get_gif_frame(carr_player_1_gif, current_frame))
    screen.blit(frame_carro_player_1, (ctrl.coluna, ctrl.linha))

    screen.blit(carro2, (coluna_carro2, linha_carro2))
    screen.blit(carro3, (coluna_carro2 - 300, linha_carro2 - 150 ))
    screen.blit(carro4, (coluna_carro2 +  100, linha_carro2 + 220 ))

    pygame.display.flip()

    #linha_pista += 100

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
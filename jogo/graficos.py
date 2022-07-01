import pygame
from pygame import font

from jogo.parametros import width, height 

FORMAT = "RGBA"

size = (width, height)
def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)

def init():
    return pygame.display.set_mode(size)


def indicador_vida(screen, cor=(0,255,0), rect=(0, 0, 200, 50) ):
    pygame.draw.rect(screen, cor, rect)

def escrever_texto(screen, posicao=(0,0), texto="texto", corTexto=(0,0,0), corFundo=(255,255,255)):
    font = pygame.font.SysFont("arial",28)   #.Font('freesansbold.ttf', 22)
    t = font.render(texto, True, corTexto, corFundo)
    textRect = t.get_rect()
    textRect.center = posicao
    screen.blit(t,textRect)

def desenha_retangulo(screen, cor=(255,255,255), rect=(230, 230, 50, 200) ):
    pygame.draw.rect(screen, cor, pygame.Rect(rect))

def desenha_circulo(screen, cor=(255,255,255), pos=(10,10)):
    pygame.draw.circle(screen, cor, pos, 100, 50 )

def desenha_inimigo(screen, rect=(200, 200, 50,50), cor=(0,0,0), filled=1):
    return pygame.draw.rect(screen, cor, rect, filled)
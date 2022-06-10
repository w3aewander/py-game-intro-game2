import pygame
from jogo import parametros as parm

def ctrl_key(keys):

    global linha
    global coluna

    if keys[pygame.K_LEFT]:
        parm.coluna -= 1

    if keys[pygame.K_RIGHT]:
        parm.coluna += 1

    if keys[pygame.K_UP]:
        parm.linha -= 1

    if keys[pygame.K_DOWN]:
        parm.linha += 1


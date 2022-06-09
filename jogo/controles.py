import pygame

coluna, linha = 400, 300

def ctrl_key(keys):

    global linha
    global coluna

    if keys[pygame.K_LEFT]:
        coluna -= 1

    if keys[pygame.K_RIGHT]:
        coluna += 1

    if keys[pygame.K_UP]:
        linha -= 1

    if keys[pygame.K_DOWN]:
        linha += 1


import pygame
pygame.mixer.init()

som_carro = pygame.mixer.Sound("sons/car-engine2.wav")
som_carro.set_volume(.8)
som_carro.play(1, 1)

size = width, height = 800, 600
linha , coluna = 0, 0

voltas = 0
velocidade = 10
coluna_pista = 0
linha_pista = 0
vida = 200

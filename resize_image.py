import pygame, sys

filename = "img/flor.jpg"
picture = pygame.image.load(filename)
picture = pygame.transform.scale(picture, (40, 60))

pygame.init()
#largura, altura
size = (800,600)
width, height = 800, 600
size = (width, height)
size = width, height = 800, 600


#Dimensoes da tela [ size ]
screen=pygame.display.set_mode(  size )

pygame.display.set_caption("Redimensionamento de imagem")

while True:

    screen.blit(picture, (0,0))
    pygame.display.update()

    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
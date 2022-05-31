import pygame
import sys
from jogo import carro

pygame.init()

width, height = 800, 600

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Meu primeiro jogo")

carro1  = carro.Carro(direcao=0, sentido=0, velocidade=10)

fundo_path = "img/fundo_tela.jpg"
carro_path = "img/seta_cima.png"

carro1.frente()
carro1.velocidade = 10

fundo = pygame.image.load(fundo_path)
car = pygame.image.load(carro1.carregar_imagem(carro_path))


coluna, linha = 350, 400

screen.blit(car, (coluna, linha))

def escrever_texto(posicao=(0,0), texto="texto", corTexto=(0,0,0), corFundo=(255,255,255)):
    font = pygame.font.Font('freesansbold.ttf', 22)
    #t = font.render(texto, True, (255,255,220), (0,190,190))
    t = font.render(texto, True, corTexto, corFundo)
    textRect = t.get_rect()
    textRect.center = posicao
    screen.blit(t,textRect)

while True:
    car = pygame.image.load(carro1.carregar_imagem(carro_path))
    screen.blit(fundo, (0, 0))
    screen.blit(car, (coluna, linha))

    s = "[{0},{1}]".format(coluna, linha)
    escrever_texto( (720,18), s)

    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        coluna -= 1
        carro_path = "img/seta_esquerda.png"
        screen.blit(car, (coluna, linha))

    if keys[pygame.K_RIGHT]:
        coluna += 1
        carro_path = "img/seta_direita.png"
        screen.blit(car, (coluna, linha))

    if keys[pygame.K_UP]:
        linha -= 1
        carro_path = "img/seta_cima.png"
        screen.blit(car, (coluna, linha))

    if keys[pygame.K_DOWN]:
        linha += 1
        carro_path = "img/seta_baixo.png"
        screen.blit(car, (coluna, linha))

    #travar o objeto na tela.
    if coluna < 0: coluna=0
    if coluna > 765: coluna=765
    if linha > 560: linha = 560
    #if linha < 409: linha= 409
    if linha < 35: linha = 35

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
           pygame.quit()
           sys.exit()

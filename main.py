import pygame
import sys
from jogo import carro

pygame.init()

width, height = 800, 600

coluna_pista = 55
linha_pista = 0


screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Meu primeiro jogo")

fundo_path = "img/pista.jpg"
carro_path = "img/carro1.png"

carro1  = carro.Carro(direcao=0, sentido=0, velocidade=10, carro_path=carro_path)

fundo = pygame.image.load(fundo_path)
carro = pygame.image.load(carro1.getImagem())

# informa o caminho para a imagem do carro
carro1.setImage(carro_path)
carro1.frente()
carro1.velocidade = 10

# define a posição do carro na tela.
coluna, linha = 150, 400
carro1.setPosition( (coluna, linha) )

screen.blit(fundo, (coluna_pista, linha_pista) )

# obtém a posição do carro
screen.blit(carro, carro1.getPosition())


pygame.display.update

# mover a pista para baixo
def mover_fundo(position=(coluna_pista, linha_pista)):
    if position[0] >= 600:
        pygame.display.flip()
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

while True:

    mover_fundo( position = (coluna_pista, linha_pista) )
    carro = pygame.image.load(carro1.getImagem())

    mover_fundo((coluna_pista, linha_pista))

    carro1.setPosition(position=(coluna, linha))
    #screen.blit(carro, carro1.getPosition())

    s = "[{0},{1}]".format(coluna, linha)
    escrever_texto( (720,18), s)

    #carro1.setPosition((coluna, linha))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        coluna -= 1
        #carro_path = "img/seta_esquerda.png"
        #carro1.setImage(carro_path)
        carro1.setPosition( position=(coluna, linha) )


    if keys[pygame.K_RIGHT]:
        coluna += 1
        #carro_path = "img/seta_direita.png"
        #carro1.setImage(carro_path)
        carro1.setPosition((coluna, linha))

    if keys[pygame.K_UP]:
        linha -= 1
        #carro_path = "img/carro1.png"
        #carro1.setImage(carro_path)
        carro1.setPosition( (coluna, linha) )


    if keys[pygame.K_DOWN]:
        linha += 1
        #carro_path = "img/seta_baixo.png"
        #carro1.setImage(carro_path)
        carro1.setPosition((coluna, linha))

    #travar o objeto na tela.
    if coluna < 0: coluna=0
    if coluna > 765: coluna=765
    if linha > 560: linha = 560
    #if linha < 409: linha= 409
    if linha < 35: linha = 35

    linha_pista += 1
    #mover_fundo( position=(coluna_pista, linha_pista))

    screen.blit(carro, (coluna, linha))
    pygame.display.update()

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
           pygame.quit()
           sys.exit()
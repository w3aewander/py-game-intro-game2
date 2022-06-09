from PIL import Image #Pillow
import pygame, sys

filename = "img/flor.jpg"
picture = pygame.image.load(filename)
picture = pygame.transform.scale(picture, (80, 120))

clock = pygame.time.Clock()

boneco_animado = Image.open("img/boneco_malabares.gif")

current_frame = 0

pygame.init()

size = width, height = 800, 600
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Redimensionamento de imagem")

FORMAT = "RGBA"

def pil_to_game(img):
    data = img.tobytes("raw", FORMAT)
    return pygame.image.fromstring(data, img.size, FORMAT)

def get_gif_frame(img, frame):
    img.seek(frame)
    return  img.convert(FORMAT)

def init():
    return pygame.display.set_mode(size)


while True:

    screen.blit(picture, (0,0))

    screen.fill( (0,0,0))

    frame_boneco = pil_to_game(get_gif_frame(boneco_animado, current_frame))
    frame_boneco = pygame.transform.scale(frame_boneco, (240, 220))
    screen.blit(frame_boneco, (30,20))
    screen.blit(frame_boneco, (270, 120))

    current_frame = (current_frame + 1) % boneco_animado.n_frames


    if not getattr(boneco_animado, "is_animated", False):
        print("Imagem em não é um gif animado")


    clock.tick(12)

    pygame.display.flip()

    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    try:
        screen = init()
        main(screen)
    finally:
        exit()
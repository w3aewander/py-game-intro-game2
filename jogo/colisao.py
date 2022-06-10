import pygame

def colisao(obj, objetos = []):
    return obj.collidelist(objetos) >= 0



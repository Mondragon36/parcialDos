import pygame as py

class Button(py.sprite.Sprite):

    def __init__(self, image1, image2, x, y):
        self.imagen_normal = image1
        self.imagen_seleccion = image2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, screen, cursor, Texto, x, y, valor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal

        screen.blit(self.imagen_actual, self.rect)
        screen.blit(Texto, (x, y))
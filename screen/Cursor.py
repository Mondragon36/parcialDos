import pygame as py

class Cursor(py.Rect):
    def __init__(self):
        py.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = py.mouse.get_pos()
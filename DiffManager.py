import pygame
from utils import *

class DiffManager:
    def __init__(self, img1, img2, bboxes, origin1, origin2):
        self.img1 = img1
        self.img2 = img2
        self.bboxes = bboxes.values()
        self.origin1 = origin1
        self.origin2 = origin2

    def click(self, location):
        loc1 = translateVector(location, scaleVector(self.origin1, -1))
        loc2 = translateVector(location, scaleVector(self.origin2, -1))

        box = None
        for bb in self.bboxes:
            if bb.collidepoint(loc1):
                self.img1.blit(self.img2, bb.topleft, bb)
                box = bb
                break
            elif bb.collidepoint(loc2):
                self.img2.blit(self.img1, bb.topleft, bb)
                box = bb
                break

        if box is not None:
            self.bboxes.remove(box)
        print len(self.bboxes)

    def isDone(self):
        return len(self.bboxes) == 0

    def draw(self, canvas):
        canvas.blit(self.img1, self.origin1)
        canvas.blit(self.img2, self.origin2)

if __name__ == '__main__':
    pass
import os
from os.path import join
import pygame
import cv2
import numpy as np
from DiffManager import DiffManager
from preproc import *

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = join(ROOT_DIR, "images")

pygame.init()
img1 = pygame.image.load(join(IMG_DIR, "img1_1.jpg"))
img2 = pygame.image.load(join(IMG_DIR, "img1_2.jpg"))
img_w, img_h = img1.get_rect().size
canvas = pygame.Surface((img_w * 2, img_h))
screen = pygame.display.set_mode((img_w * 2, img_h))
img1 = img1.convert()
img2 = img2.convert()
mask = cv2.imread(join(IMG_DIR, "img1_mask.png"), 0)
print "bboxes"
indices, newidx = indexObjects(mask)
bboxes = boundingBoxes(indices)
print "bboxes done"
dm = DiffManager(img1, img2, bboxes, canvas, (0, 0), (img_w, 0))
canvas = canvas.convert()
canvas.fill((255, 128, 0))
done = False

clock = pygame.time.Clock()
dm.draw()
screen.blit(canvas, (0, 0))

found_list = set()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            loc = pygame.mouse.get_pos()
            dm.click(loc)
            if len(dm.bboxes) == 0:
                done = True

    dm.draw()
    screen.fill((255, 128, 0))
    screen.blit(dm.canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)
import os
from os.path import join
import pygame
from DiffManager import DiffManager
from preproc2 import *
import level_data
import random
from cache import get_cache

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = join(ROOT_DIR, "images")
IMG_RESOLUTION = 600, 900
levels = level_data.get_levels()


def main():
    pygame.init()
    level = levels[random.randint(0, len(levels) - 1)]
    img1 = pygame.image.load(join(IMG_DIR, level[0]))
    img2 = pygame.image.load(join(IMG_DIR, level[1]))
    img_w, img_h = IMG_RESOLUTION
    canvas = pygame.Surface((img_w * 2, img_h))
    screen = pygame.display.set_mode((img_w * 2, img_h))
    img1 = img1.convert()
    img2 = img2.convert()
    print "bboxes"
    maskfile = join(IMG_DIR, level[2])
    bboxes = get_cache(maskfile, get_bboxes)
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
    pygame.quit()


def get_bboxes(maskfile):
    mask = pygame.image.load(maskfile).convert()
    indices, newidx = indexObjects(mask)
    bboxes = boundingBoxes(indices)
    return bboxes


if __name__ == '__main__':
    main()
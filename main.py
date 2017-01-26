import os
from os.path import join
import pygame
from DiffManager import DiffManager
from preproc2 import *
import level_data
import random
import cache
import resources

resources.ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
resources.IMG_DIR = join(resources.ROOT_DIR, "images")
resources.IMG_RESOLUTION = 600, 900
levels = level_data.get_levels()

def main():
    pygame.init()
    level = levels[random.randint(0, len(levels) - 1)]
    img1 = pygame.image.load(join(resources.IMG_DIR, level[0]))
    img2 = pygame.image.load(join(resources.IMG_DIR, level[1]))
    img_w, img_h = resources.IMG_RESOLUTION
    canvas = pygame.Surface((img_w * 2, img_h))
    screen = pygame.display.set_mode((img_w * 2, img_h))
    img1 = img1.convert()
    img2 = img2.convert()
    canvas = canvas.convert()
    canvas.fill((255, 128, 0))
    print "bboxes"
    maskfile = join(resources.IMG_DIR, level[2])
    bboxes = cache.get_cache(maskfile, get_bboxes)
    print "bboxes done"
    dm = DiffManager(img1, img2, bboxes, (0, 0), (img_w, 0))
    done = False
    clock = pygame.time.Clock()
    dm.draw(canvas)
    screen.blit(canvas, (0, 0))
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

        dm.draw(canvas)
        screen.fill((255, 128, 0))
        screen.blit(canvas, (0, 0))

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
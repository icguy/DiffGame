import os
from os.path import join
import pygame
from DiffManager import DiffManager
from preproc2 import *
import level_data
import random
import cache
import resources
import SceneManagement as scene
import Scenes.LevelScene as levelScene

resources.ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
resources.IMG_DIR = join(resources.ROOT_DIR, "images")
resources.IMG_RESOLUTION = 600, 900
levels = level_data.get_levels()

def main():
    pygame.init()
    level = levels[random.randint(0, len(levels) - 1)]
    level = levels[1]
    img_w, img_h = resources.IMG_RESOLUTION
    canvas = pygame.Surface((img_w * 2, img_h))
    screen = pygame.display.set_mode((img_w * 2, img_h))
    canvas = canvas.convert()
    canvas.fill((255, 128, 0))
    done = False
    clock = pygame.time.Clock()

    sceneManager = scene.SceneManager()
    level_scene = levelScene.LevelScene(sceneManager, level)
    sceneManager.registerScene(level_scene)
    sceneManager.updateScene(level_scene)

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
                sceneManager.click(loc)
        #update
        sceneManager.update()

        #draw
        sceneManager.draw(canvas)
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
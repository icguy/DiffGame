import SceneManagement
import pygame

from os.path import join
from DiffManager import DiffManager
from preproc2 import *
from cache import get_cache
import resources

class LevelScene(SceneManagement.Scene):
    def __init__(self, manager, level, nextLevelName = None):
        SceneManagement.Scene.__init__(self, manager)
        self.level = level
        self.name = level[0]
        self.diffManager = None
        self.loaded = False
        self.nextLevelName = nextLevelName

    def load(self):
        if self.loaded:
            return

        img1 = pygame.image.load(join(resources.IMG_DIR, self.level[0]))
        img2 = pygame.image.load(join(resources.IMG_DIR, self.level[1]))
        img_w, img_h = resources.IMG_RESOLUTION
        img1 = img1.convert()
        img2 = img2.convert()
        print "bboxes"
        maskfile = join(resources.IMG_DIR, self.level[2])
        bboxes = get_cache(maskfile, None)
        print "bboxes done"
        self.diffManager = DiffManager(img1, img2, bboxes, (0, 0), (img_w, 0))
        self.loaded = True

    def unload(self):
        if not self.loaded:
            return

        self.diffManager = None
        self.loaded = False

    def draw(self, canvas):
        self.diffManager.draw(canvas)

    def update(self):
        pass

    def click(self, pos):
        self.diffManager.click(pos)
        if self.diffManager.isDone():
            pass #todo add transition animation

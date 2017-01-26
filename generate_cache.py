import level_data
import main
import cache
import pygame
from os.path import join
import resources

pygame.init()
levels = level_data.get_levels()
for level in levels:
    print level
    maskfile = join(resources.IMG_DIR, level[2])
    bboxes = cache.get_cache(maskfile, main.get_bboxes)
    print "bboxes done"
pygame.quit()
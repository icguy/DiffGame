import os
from os.path import join
import pygame

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
IMG_DIR = join(ROOT_DIR, "images")

pygame.init()
img1 = pygame.image.load(join(IMG_DIR, "img1_1.jpg"))
img2 = pygame.image.load(join(IMG_DIR, "img1_2.jpg"))
img_mask = pygame.image.load(join(IMG_DIR, "img1_mask.png"))
img_w, img_h = img1.get_rect().size
canvas = pygame.Surface((img_w * 2, img_h))
screen = pygame.display.set_mode((img_w * 2, img_h))
img1 = img1.convert()
img2 = img2.convert()
img_mask = img_mask.convert()
canvas = canvas.convert()
done = False
# is_blue = True
# is_img = False
# x = 30
# y = 30

rect_dict = {
    1 : pygame.Rect(30, 187, 48, 53),
    2 : pygame.Rect(92, 173, 64, 84),
    3 : pygame.Rect(411, 92, 83, 102),
    4 : pygame.Rect(443, 255, 53, 51),
    5 : pygame.Rect(510, 357, 52, 50)
}

clock = pygame.time.Clock()
canvas.blit(img1, (0, 0))
canvas.blit(img2, (img_w, 0))

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
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x %= img_w
            mask_color = img_mask.get_at((mouse_x, mouse_y))
            idx = mask_color[2]
            print mask_color, idx
            if idx != 0:
                found_list.add(idx)
                if(len(found_list)) == 5:
                    done = True
                    break
                    
                rect = rect_dict[idx]
                print rect, rect.topleft
                canvas.blit(img2, rect.topleft, rect)

    screen.fill((0, 0, 0))

    screen.blit(canvas, (0, 0))

    pygame.display.flip()
    clock.tick(60)
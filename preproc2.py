import pygame

# todo wipe out opencv from this code

def get_max(img):
    w, h = img.get_size()
    return max([max([max(img.get_at((i, j))[:3]) for i in range(w)]) for j in range(h)])

def zeros(w, h):
    surf = pygame.Surface((w, h))
    surf.fill((0, 0, 0))
    return surf

def boundingBoxes(diff_img, vals = None):
    idx_dict = {}
    if vals is None:
        maxidx = get_max(diff_img)
        vals = range(1, maxidx + 1)

    for i in vals:
        bbox = getBoundingBox(diff_img, (i, i, i))
        if bbox is not None:
            idx_dict[i] = bbox
    return idx_dict

def inBounds(img, r, c):
    w, h = img.get_size()
    return 0 <= c < w and 0 <= r < h

def isBlack(img, c, r):
    color = img.get_at((c, r))
    threshold = 60
    return threshold > sum(color[:3])

def indexObjects(img):
    indices = zeros(*img.get_size())
    toCheck = []

    w, h = img.get_size()
    newIdx = 1

    for r in range(h):
        for c in range(w):
            if not isBlack(img, c, r) and indices.get_at((c, r)) == (0, 0, 0):
                toCheck.append((c, r))
                while len(toCheck) > 0:
                    cc, cr = toCheck[0]
                    if not inBounds(img, cr, cc):
                        toCheck.pop(0)
                        continue

                    if not isBlack(img, cc, cr) and indices.get_at((cc, cr)) == (0, 0, 0):
                        indices.set_at((cc, cr), (newIdx, newIdx, newIdx))
                        toCheck.append((cc - 1, cr))
                        toCheck.append((cc + 1, cr))
                        toCheck.append((cc, cr - 1))
                        toCheck.append((cc, cr + 1))

                    toCheck.pop(0)
                newIdx += 1
    return indices, newIdx

def getBoundingBox(img, val = (255, 255, 255)):
    w, h = img.get_size()
    U = h
    D = 0
    L = w
    R = 0
    found = False
    for r in range(h):
        for c in range(w):
            if img.get_at((c, r)) == val:
                found = True
                if r < U:
                    U = r
                if r > D:
                    D = r
                if c < L:
                    L = c
                if c > R:
                    R = c
    if not found:
        return None

    return pygame.Rect(L, U, R-L, D-U)

def test():
    pygame.init()
    img = pygame.image.load("images/img1_mask.jpg")
    w, h = img.get_size()
    screen = pygame.display.set_mode((w, h))
    img = img.convert()
    clock = pygame.time.Clock()

    indices, newidx = indexObjects(img)
    bboxes = boundingBoxes(indices)

    for i in bboxes:
        bbox = bboxes[i]
        U, D, L, R = bbox.top, bbox. bottom, bbox.left, bbox.right
        pygame.draw.rect(img, (255, 128, 0), pygame.Rect(L, U, (R-L), (D-U)))

        font = pygame.font.Font(None, 36)
        text = font.render(str(i), 1, (0, 128, 255))
        textpos = text.get_rect()
        textpos.right = L
        textpos.bottom = U
        img.blit(text, textpos)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.KEYDOWN:
                done = True
                break

        screen.fill((255, 128, 0))
        screen.blit(img, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    test()
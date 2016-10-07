import numpy as np
import cv2
import pygame

def boundingBoxes(diff_img, vals = None):
    idx_dict = {}
    if vals is None:
        maxidx = np.max(diff_img)
        vals = range(1, maxidx + 1)

    for i in vals:
        bbox = getBoundingBox(diff_img, i)
        if bbox is not None:
            idx_dict[i] = bbox
    return idx_dict

def inBounds(img, r, c):
    h, w = img.shape[0], img.shape[1]
    return 0 <= c < w and 0 <= r < h

def indexObjects(img):
    indices = np.zeros(img.shape, 'uint8')
    toCheck = []

    h, w = img.shape
    newIdx = 1

    for r in range(h):
        for c in range(w):
            if img[r, c] > 0 and indices[r, c] == 0:
                toCheck.append((c, r))
                while len(toCheck) > 0:
                    cc, cr = toCheck[0]
                    if not inBounds(img, cr, cc):
                        toCheck.pop(0)
                        continue

                    if img[cr, cc] > 0 and indices[cr, cc] == 0:
                        indices[cr, cc] = newIdx
                        toCheck.append((cc - 1, cr))
                        toCheck.append((cc + 1, cr))
                        toCheck.append((cc, cr - 1))
                        toCheck.append((cc, cr + 1))

                    toCheck.pop(0)
                newIdx += 1
    return indices, newIdx

def getBoundingBox(img, val = 255):
    h, w = img.shape
    U = h
    D = 0
    L = w
    R = 0
    found = False
    for r in range(h):
        for c in range(w):
            if img[r, c] == val:
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
    diff = cv2.imread("images/img1_mask.png", 0)
    indices, newidx = indexObjects(diff)
    bboxes = boundingBoxes(indices)
    for i in bboxes:
        bbox = bboxes[i]
        U, D, L, R = bbox.top, bbox. bottom, bbox.left, bbox.right
        cv2.rectangle(diff, (L, U), (R, D), 255)
        cv2.putText(diff, str(i), (L, D), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
    cv2.imshow("asd", diff)
    cv2.waitKey()


if __name__ == '__main__':
    test()
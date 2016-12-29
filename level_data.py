from os import listdir
from os.path import splitext
import main

def get_names(img1):
    basename, ext = splitext(img1)
    basename = basename[:-2]
    return ("%s%s%s" % (basename, "_1", ext),
            "%s%s%s" % (basename, "_2", ext),
            "%s%s%s" % (basename, "_mask", ext))

def get_levels():
    return [get_names(img) for img in listdir(main.IMG_DIR) if splitext(img)[0].endswith("_1")]

if __name__ == '__main__':
    print get_levels()
from os import listdir
from os.path import splitext

def get_names(img1):
    basename, ext = splitext(img1)
    basename = basename[:-2]
    return ("%s%s%s" % (basename, "_1", ext),
            "%s%s%s" % (basename, "_2", ext),
            "%s%s%s" % (basename, "_mask", ext))

def get_levels():
    import main
    """
    :return: list of 3-tuples: ("level_1.png", "level_2.png", "level_mask.png")
    """
    return [get_names(img) for img in listdir(main.IMG_DIR) if splitext(img)[0].endswith("_1")]

if __name__ == '__main__':
    print get_levels()
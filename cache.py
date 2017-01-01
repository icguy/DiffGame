import pickle
from os.path import exists, splitext

def get_cache(filename, function):
    cache_file = splitext(filename)[0] + ".p"
    if exists(cache_file):
        print "cache: reading cache"
        try:
            with file(cache_file) as f:
                return pickle.load(f)
        except:
            print "cache: error. unable to read file"

    print "cache: calling processing func"
    data = function(filename)
    try:
        with file(cache_file, "w") as f:
            print "cache: dumping data"
            pickle.dump(data, f)
    except:
        print "cache: error. unable to write data"
    return data


def test():
    data = "asd"
    testmethod = lambda x: x + "qwe"
    print get_cache(data, testmethod)

if __name__ == '__main__':
    test()

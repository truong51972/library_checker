def readScaleFile():
    f = open('./setting/scale.size', 'r')
    size = int(f.read())
    f.close()
    return size

def translateVector(vec, delta):
    px, py = vec
    dx, dy = delta
    return px + dx, py + dy

def scaleVector(vec, scale):
    x, y = vec
    return x * scale, y * scale
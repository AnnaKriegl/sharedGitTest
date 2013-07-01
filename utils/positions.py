from math import cos, sin

def grid(x, y, z):
    """ Returns a list of positions to fill up a 3D grid. """
    return [[a,b,c] for a in range(x) for b in range(y) for c in range(z)]

def spiral(n=10, radius=1, step=0.1, heightStep=0.1):
    return [[cos(x*step)*radius, x*heightStep, sin(x*step)*radius] for x in range(n)]

def spiralIter(n=10, radius=1, step=0.1, heightStep=0.1):
    return ((cos(x*step)*radius, x*heightStep, sin(x*step)*radius) for x in range(n))

def gridIter(x, y, z):
    """ Returns an iterator/generator that yields positions in a 3D grid defined by x, y and z. """
    return ((a, b, c) for a in xrange(x) for b in xrange(y) for c in xrange(z))
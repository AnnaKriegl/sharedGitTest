import maya.cmds as mc

def polyCubeRange(xx):
    for x in range(xx):
        mc.polyCube()

def polyPrismRange(xx):
    for x in range(xx):
        mc.polyPrism()

def createSphere():
    mc.polySphere()

def grid(x, y, z):
    """ Returns a list of positions to fill up a 3D grid. """
    return [[a,b,c] for a in range(x) for b in range(y) for c in range(z)]

def gridIter(x, y, z):
    """ Returns an iterator/generator that yields positions in a 3D grid defined by x, y and z. """
    return (a, b, c for a in xrange(x) for b in xrange(y) for c in xrange(z))

def cubeGrid(x, y, z):
    for p in gridIter(x,y,z):
        obj = mc.polyCube()[0]
        mc.xform(obj, t=p)

def sphereGrid(x, y, z):
    for p in gridIter(x,y,z):
        obj = mc.polySphere()[0]
        mc.xform(obj, t=p)
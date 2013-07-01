import maya.cmds as mc
from utils.positions import grid, spiral, gridIter, spiralIter

def polyCubeRange(xx):
    for x in range(xx):
        mc.polyCube()

def polyPrismRange(xx):
    for x in range(xx):
        mc.polyPrism()

def createSphere():
    mc.polySphere()

def createOnPos(createFunc, posIter):
    L = []
    for p in posIter:
        obj = createFunc()
        mc.xform(obj, t=p)
        L.extend(obj)
    return L

def cubeGrid(x, y, z):
    return createOnPos(mc.polyCube, gridIter(x, y, z))

def sphereGrid(x, y, z):
    return createOnPos(mc.polySphere, gridIter(x, y, z))


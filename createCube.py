import maya.cmds as mc
from functools import partial
from utils.positions import grid, spiral, gridIter, spiralIter

def polyCubeRange(xx): #RAANGER
    for x in range(xx):
        mc.polyCube()

def polyPrismRange(xx):
    for x in range(xx):
        mc.polyPrism()

print "hello octocat"

def createSphere():
    mc.polySphere()

print "how does this work?!?!?!?!?!??!?!"

def sumyInYourTummy(foodA, foodB):
    return foodA + foodB

partial(sumyInYourTummy, 1, 2)

f = 10

def makeSunshine():
    clouds = False
    if not clouds:
        sun = True
        return sun


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


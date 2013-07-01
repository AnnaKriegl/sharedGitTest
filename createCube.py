import maya.cmds as mc
from functools import partial

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


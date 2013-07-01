import maya.cmds as mc

def polyCubeRange(xx):
    for x in range(xx):
        mc.polyCube()

def polyPrimsRange(xx):
    for x in range(xx):
        mc.polyPrism()

def createSphere():
    mc.polySphere()

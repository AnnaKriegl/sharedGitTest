import maya.cmds as mc

def polyCubeRange(xx):
    for x in range(xx):
        mc.polyCube()

def createSphere():
    mc.polySphere()

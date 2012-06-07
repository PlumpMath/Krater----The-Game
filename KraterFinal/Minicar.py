import direct.directbase.DirectStart
from panda3d.core import CollisionHandlerQueue,CollisionRay,CollisionSphere,CollisionPolygon
from panda3d.core import CollisionTraverser,CollisionNode,CollisionTube
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence
from pandac.PandaModules import TransparencyAttrib
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import Vec3,Vec4,BitMask32
from direct.actor.Actor import Actor
from panda3d.core import Point3
from math import pi, sin, cos
import random, sys, os, math
from direct.task import Task
import MoveMC
from MoveMC import *


class Minicar():

    def __init__(self):

        base.camera.setZ( base.camera, 3 * globalClock.getDt() ) # Initialization CameraZ
        base.camera.setY( base.camera, -10 * globalClock.getDt() ) # Initialization CameraY

        """  -------------------- Load The Principal Actor ---------------------- """

        # It's the Actor In the Game.
        
        self.jeep = Actor( "modelos/jeep/jeep",
                           {"walk": "modelos/jeep/jeep-start"})
        self.jeep.setScale(0.7)
        self.jeep.setPos(0,30,-6.8)
        self.jeep.reparentTo(render)
        self.jeep.setH( 180.0 )
        
        """ --------------------------------------------------------------------- """

        self.moving = MoveMC(self.jeep)


    

    def getMinicar(self):
        return self.jeep

import direct.directbase.DirectStart
from panda3d.core import CollisionHandlerQueue,CollisionRay,CollisionSphere,CollisionPolygon
from panda3d.core import CollisionTraverser,CollisionNode,CollisionTube
from panda3d.core import Filename,AmbientLight,DirectionalLight
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


class Items:

    def __init__(self):

        self.energy = []

        """  ---------------------------- Load Energy --------------------------- """

        # Charge models of the energy bottle.
        
        cont = 0
        while( cont < 200 ):
            self.energy.append( loader.loadModel("modelos/energia/energia") )
            cont = cont + 1

        """ --------------------------------------------------------------------- """
        
        
        """  ------------------ Load posicions of the bottles ------------------- """
        
        cont = 0
        while( cont < 80 ):
            x = random.randint(-26, 26)
            y = random.randint( 0, 24090)
            self.energy[cont].reparentTo(render)
            self.energy[cont].setScale(.5)
            self.energy[cont].setPos( x, y, 0)
            self.energy[cont].setH( 270.0 )
            cont = cont + 1
            
        """ --------------------------------------------------------------------- """

    def getEnergy( self ):
        return self.energy

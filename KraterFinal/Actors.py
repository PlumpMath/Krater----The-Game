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


class Actors:

    def __init__(self):

        self.bombero = []
        self.balloons = []

        """  -------------------- Load The Secondary Actor ---------------------- """

        # This actor is the narrator of the game.

        """self.broman = Actor( "modelos/tutman/bullyactormodel",
                             {"ani": "modelos/tutman/bullyactoranimpieceofcrap",
                              "ani2": "modelos/tutman/bullyactoranimnoneofthese",
                              "ani3": "modelos/tutman/bullyactoranimfoodstamps",
                              "ani4": "modelos/tutman/bullyactoranimbeatme"})
        self.broman.setScale(15.0)
        self.broman.setPos(0,100,1.0)
        self.broman.reparentTo(render)
        # Loop its animation.
        self.broman.loop("ani2")
        self.broman.setH( 90.0 )"""

        """ --------------------------------------------------------------------- """

        """  -------------------- Load The Secondary Actor ---------------------- """

        # These are children who run for the sidewalk
        
        cont = 1
        posIni = -3400
        while( cont < 40 ):
            self.bombero.append( Actor( "modelos/bombero/bombero",
                                {"ani": "modelos/bombero/bombero1",
                                 "ani2": "modelos/bombero/bombero2",
                                 "ani3": "modelos/bombero/bombero3"}) )
            self.bombero[cont-1].reparentTo(render)
            self.bombero[cont-1].setScale(1.0)
            if( (cont % 2) == 0 ): self.bombero[cont-1].setPos(-26,posIni,-7.0)
            else: self.bombero[cont-1].setPos(24,posIni,-7.0)
            self.bombero[cont-1].loop("ani2")
            self.bombero[cont-1].setH( 180.0 )
            posIni= posIni + 600
            cont = cont + 1
            
        """ --------------------------------------------------------------------- """

        """  -------------------- Load The Secondary Actor ---------------------- """

        # These are children who have balloons.
        
        cont = 0
        while( cont < 50 ):
            self.balloons.append( Actor( "modelos/nino/nino",
                                 {"ani": "modelos/nino/nino2"}) )
            self.balloons[cont].reparentTo(render)
            self.balloons[cont].setScale(.05)
            self.balloons[cont].setPos(30, 100+(308*(cont*2)),3.0)
            self.balloons[cont].loop("ani")
            self.balloons[cont].setH( 270.0 )
            cont = cont + 1
            
        """ --------------------------------------------------------------------- """

        taskMgr.add(self.runBombero, "runBombero")

    def runBombero(self, task):
        next = 0
        while( next < 39 ):
            self.bombero[next].setY( self.bombero[next].getY() + 8 )
            next = next + 1
        return Task.cont

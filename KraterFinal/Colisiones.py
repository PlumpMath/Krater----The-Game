import direct.directbase.DirectStart
from panda3d.core import CollisionHandlerQueue,CollisionRay,CollisionSphere,CollisionPolygon
from panda3d.core import CollisionTraverser,CollisionNode,CollisionTube
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import TextNode
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


def addText(pos1, pos2, msg, scl):
    return OnscreenText(text=msg, style=2, fg=(1,1,1,1),
                        pos=(pos2, pos1), align=TextNode.ALeft, scale = scl)

texta = addText( 0.9, -1.2,  "Hasta Ahora LLevamos " + "0" + " Bebidas", 0.07 )

class Colisiones:

    def __init__(self, energy, jeep):

        self.bebidas = 0
        self.energy = energy
        self.crash = []
        self.jeep = jeep

        """  ---------------------- Prepara las Colisiones ---------------------- """
        
        self.cs = CollisionSphere(0, 0, 0, 20)
        cont = 0
        while( cont < 80 ):
            self.crash.append( self.energy[cont].attachNewNode(CollisionNode(str(cont))) )
            self.crash[cont].node().addSolid(self.cs)
            #self.crash[cont].show() Uncomment this line to see the colisions
            cont = cont + 1

        self.css = CollisionSphere(0, 0, 0, 12)
        self.cnodePath = self.jeep.attachNewNode(CollisionNode('cnode'))
        self.cnodePath.node().addSolid(self.css)

        #self.cnodePath.show() Uncomment this line to see the colisions

        self.traverser = CollisionTraverser()
        self.queue = CollisionHandlerQueue()
        
        """ --------------------------------------------------------------------- """

        taskMgr.add(self.choque, "choque")

    def choque(self, task):
        
        self.traverser.addCollider(self.cnodePath, self.queue)
        self.traverser.traverse(render)
        for i in range(self.queue.getNumEntries()):
            entry = self.queue.getEntry(i)
            self.energy[int( entry.getIntoNode().getName() )].setPos(0,0,5000)
            self.bebidas = self.bebidas + 1
            global texta
            texta.destroy()
            texta = addText( 0.9, -1.2,  "Hasta Ahora LLevamos " + str(self.bebidas) + " Bebidas", 0.07 )
        return Task.cont

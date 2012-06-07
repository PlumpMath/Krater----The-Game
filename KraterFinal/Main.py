import direct.directbase.DirectStart
from panda3d.core import TextNode
from direct.showbase.DirectObject import DirectObject
from pandac.PandaModules import TransparencyAttrib
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
import World, Items, Colisiones, Actors
from World import *
from Items import *
from Colisiones import *
from Actors import *

class Game(DirectObject):

    def __init__(self):

        base.disableMouse()
        self.world      = World()
        self.items      = Items()
        self.energy     = self.items.getEnergy()
        self.minicar    = self.world.getMinicar()
        self.colisiones = Colisiones( self.energy, self.minicar )
        self.actores    = Actors()

w = Game()
run()



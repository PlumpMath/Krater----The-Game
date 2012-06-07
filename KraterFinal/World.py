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
import Minicar
from Minicar import *


class World:

    def __init__(self):
        
        self.separators = []
        self.statua = []
        self.lamp = []
        self.terrain = []
        self.idStop = 0
        self.mayor = 190.0
        self.minicar = Minicar()
        self.jeep = self.minicar.getMinicar()

        self.buildings = [  loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("modelos/building/building"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa7/dojo"),
                            loader.loadModel("edificios/casas/casa12/funhouse"),
                            loader.loadModel("edificios/casas/casa13/ringtoss")]


        """  ---------------------------- Load the World ------------------------ """

        # this section of rendering will be extract in one class extern the wich
        # instace a segment of world acord to the position of the character.

        cont = 0
        while( cont < 79 ):
            self.terrain.append( loader.loadModel("modelos/pista/calle") )
            self.terrain[cont].reparentTo(render)
            self.terrain[cont].setScale(25)
            self.terrain[cont].setPos(-85, 130 + (308*cont), -69)
            cont = cont + 1
        
        """ --------------------------------------------------------------------- """


        """  ---------------------------- Load Buildings ------------------------ """

        # Load all buildings in the Game for segments the last two of each part
        # Are diferents. PD. each part have 3 segments and each segment have
        # 5 buildings.

        cont = 0
        conta = -1
        while( cont < 200 ):
            self.buildings[cont].reparentTo(render)
            conta = conta + 1
    
            if( conta == 4 ):
                self.buildings[cont].setScale(3.5)
                self.buildings[cont].setPos(-68, 380+((308*((cont)/5)*2)), -8)
                self.buildings[cont].setH( 90.0 )
                conta = -1
            if( conta == 3 ):
                self.buildings[cont].setScale(.8)
                self.buildings[cont].setPos(32, 338+((308*((cont)/5)*2)), -8)
                self.buildings[cont].setH( 180.0 )
            if( conta == 2 ):
                self.buildings[cont].setScale(.2)
                self.buildings[cont].setPos(80, 295+((308*((cont)/5)*2)), -8)
                self.buildings[cont].setH( 90.0 )
            if( conta == 1 ):
                self.buildings[cont].setScale(.2)
                self.buildings[cont].setPos(-85, 295+((308*((cont)/5)*2)), -8)
                self.buildings[cont].setH( 270.0 )
            if( conta == 0 ):
                self.buildings[cont].setScale(.5)
                self.buildings[cont].setPos(-34, 260+((308*((cont)/5)*2)), -8)
            cont = cont + 1

        cont = 1
        while( cont < 14 ):
            self.buildings[(cont*15)-2].setScale(5.2)
            self.buildings[(cont*15)-2].setPos(96, 375+(cont*(308*4))+13, -8)
            self.buildings[(cont*15)-2].setH( 180.0 )
            self.buildings[(15*cont)-1].setScale(3.2)
            self.buildings[(15*cont)-1].setPos(-85, 380+(cont*(308*4))+8, -8)
            self.buildings[(15*cont)-1].setH( 180.0 )
            cont = cont + 1
            
            
        """ --------------------------------------------------------------------- """


        """  ---------------------------- Load Separators ----------------------- """
        
        # Charge the Models of the separators between two segments of terrain only
        # only charge 8 and move the first 4 in the time.
        
        cont = 0
        ident = -1
        while( cont < 16 ):
            self.separators.append( loader.loadModel("modelos/separador/roadblock") )
            self.separators[cont].reparentTo(render)
            self.separators[cont].setScale(1.0)
            self.separators[cont].setH( 90.0 )
            posi = (308*int(cont/8))
            ident = ident + 1
            if( ident == 0 ): self.separators[cont].setPos(37, posi+137, -8)
            if( ident == 1 ): self.separators[cont].setPos(37, posi+152, -8)
            if( ident == 2 ): self.separators[cont].setPos(37, posi+167, -8)
            if( ident == 3 ): self.separators[cont].setPos(37, posi+182, -8)
            if( ident == 4 ): self.separators[cont].setPos(-38, posi+137, -8)
            if( ident == 5 ): self.separators[cont].setPos(-38, posi+152, -8)
            if( ident == 6 ): self.separators[cont].setPos(-38, posi+167, -8)
            if( ident == 7 ):
                self.separators[cont].setPos(-38, posi+182, -8)
                ident = -1
            cont = cont + 1

        """ --------------------------------------------------------------------- """


        """  ---------------------------- Load Objects ------------------------- """

        # Charge the estatuas , lamparas , hidrantes, etc in the world.
        
        cont = 0
        while( cont < 50 ):
            self.statua.append( loader.loadModel("modelos/estatua/estatua") )
            self.lamp.append( loader.loadModel("modelos/lampara/lampara") )
            self.statua[cont].reparentTo(render)
            self.lamp[cont].reparentTo(render)
            self.statua[cont].setScale(4.0)
            self.lamp[cont].setScale(4.0)
            self.statua[cont].setPos(-38, 95+(308*(cont*2)), -8)
            self.lamp[cont].setPos(-38, 115+(308*(cont*2)), -8)
            self.statua[cont].setH( 270.0 )
            self.lamp[cont].setH( 270.0 )
            cont = cont + 1

        """ --------------------------------------------------------------------- """

        #taskMgr.add(self.stopSignal, "stopSignal")
        

    def stopSignal(self,task):
        if( self.jeep.getY() > self.mayor  ):
            self.mayor = (self.mayor + 308)
            if( self.idStop == 0 ):
                self.separators[0].setY( self.separators[0].getY() + 616 )
                self.separators[1].setY( self.separators[1].getY() + 616 )
                self.separators[2].setY( self.separators[2].getY() + 616 )
                self.separators[3].setY( self.separators[3].getY() + 616 )
                self.separators[4].setY( self.separators[4].getY() + 616 )
                self.separators[5].setY( self.separators[5].getY() + 616 )
                self.separators[6].setY( self.separators[6].getY() + 616 )
                self.separators[7].setY( self.separators[7].getY() + 616 )
                self.idStop = 1
            else:
                self.separators[8].setY( self.separators[8].getY() + 616 )
                self.separators[9].setY( self.separators[9].getY() + 616 )
                self.separators[10].setY( self.separators[10].getY() + 616 )
                self.separators[11].setY( self.separators[11].getY() + 616 )
                self.separators[12].setY( self.separators[12].getY() + 616 )
                self.separators[13].setY( self.separators[13].getY() + 616 )
                self.separators[14].setY( self.separators[14].getY() + 616 )
                self.separators[15].setY( self.separators[15].getY() + 616 )
                self.idStop = 0
        return Task.cont

        
    def getTerrain(self):
        return self.terrain

    def getMinicar(self):
        return self.jeep

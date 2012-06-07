import direct.directbase.DirectStart
from panda3d.core import CollisionTraverser,CollisionNode,CollisionTube
from panda3d.core import CollisionHandlerQueue,CollisionRay,CollisionSphere,CollisionPolygon
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from direct.task import Task
from math import pi, sin, cos
from direct.gui.OnscreenImage import OnscreenImage
from pandac.PandaModules import TransparencyAttrib
import time


def addText(pos1, pos2, msg, scl):
    return OnscreenText(text=msg, style=2, fg=(1,1,1,1),
                        pos=(pos2, pos1), align=TextNode.ALeft, scale = scl)

text = OnscreenText(text = '', pos = (-0.5, 0.02), scale = 0.07)
texta = addText( 0.9, -1.2,  "Hasta Ahora LLevamos " + "0" + " Bebidas", 0.07 )
tempo = addText( 0.9, 0.3,  "Tiempo Trascurrido: 0.0 Seg", 0.07 )
 
class Draw(DirectObject):

    def __init__(self):

        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}

        self.separators = []
        self.crash = []
        self.statua = []
        self.lamp = []
        self.terrain = []
        self.bombero = []
        self.energy = []
        self.balloons = []

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
        
        self.angleDegrees = 0
        self.isMoving = False
        self.isCollision = False
        self.mayor = 190.0
        self.bebidas = 0
        self.idStop = 0
        self.textIni = 0
        self.Perdio = 0
        self.sonidito = 0
        self.activate = 0
        base.disableMouse()
        base.camera.setZ( base.camera, 3 * globalClock.getDt() ) # Initialization CameraZ
        base.camera.setY( base.camera, -10 * globalClock.getDt() ) # Initialization CameraY
        
        """self.Lvl1 = base.loader.loadSfx("tales.mp3")
        self.Lvl1.setLoop(True)
        self.Lvl1.setVolume(0.0)
        self.Lvl1.play()"""

        self.Lvl2 = base.loader.loadSfx("vel3.wav")
        self.Lvl2.setLoop(True)
        self.Lvl2.setVolume(0.6)


        self.Lvl4 = base.loader.loadSfx("instru.wav")
        self.Lvl4.setLoop(False)
        self.Lvl4.setVolume(1.0)

        self.punch = base.loader.loadSfx("punch.mp3")
        self.punch.setVolume(1.0)

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


        """  ---------------------------- Load Energy --------------------------- """

        # Charge models of the energy bottle.
        
        cont = 0
        while( cont < 200 ):
            self.energy.append( loader.loadModel("modelos/energia/energia") )
            cont = cont + 1

        """ --------------------------------------------------------------------- """


        """  -------------------- Load The Principal Actor ---------------------- """

        # It's the Actor In the Game.
        
        self.jeep = Actor( "modelos/jeep/jeep",
                           {"walk": "modelos/jeep/jeep-start"})
        self.jeep.setScale(0.7)
        self.jeep.setPos(0,30,-6.8)
        self.jeep.reparentTo(render)
        self.jeep.setH( 180.0 )
        
        """ --------------------------------------------------------------------- """



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
            

        """  ---------------------- Prepara las Colisiones ---------------------- """
        
        self.cs = CollisionSphere(0, 0, 0, 15)
        cont = 0
        while( cont < 80 ):
            self.crash.append( self.energy[cont].attachNewNode(CollisionNode(str(cont))) )
            self.crash[cont].node().addSolid(self.cs)
            #self.crash[cont].show()
            cont = cont + 1

        self.css = CollisionSphere(0, 0, 0, 12)
        self.cnodePath = self.jeep.attachNewNode(CollisionNode('cnode'))
        self.cnodePath.node().addSolid(self.css)

        #self.cnodePath.show()
        #self.cnodePath.show()

        self.traverser = CollisionTraverser()
        self.queue = CollisionHandlerQueue()
        
        """ --------------------------------------------------------------------- """        


        """  ----------------- when do you pressed one key ---------------------- """

        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["forward",1])
        self.accept("a", self.setKey, ["cam-left",1])
        self.accept("s", self.setKey, ["cam-right",1])
        self.accept("r", self.setKey, ["look-back",1])
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["forward",0])
        self.accept("a-up", self.setKey, ["cam-left",0])
        self.accept("s-up", self.setKey, ["cam-right",0])
            
        """ --------------------------------------------------------------------- """


        taskMgr.add(self.move, "move")
        taskMgr.add(self.follow, "follow")
        taskMgr.add(self.stopSignal, "stopSignal")
        taskMgr.add(self.runBombero, "runBombero")
        taskMgr.add(self.collision, "collision")



    def runBombero(self, task):
        next = 0
        while( next < 39 and self.Perdio == 0 ):
            self.bombero[next].setY( self.bombero[next].getY() + 8 )
            next = next + 1
        return Task.cont

    
    def collision(self, task):
        """if( (160 - time.clock()) >= 150 and self.Perdio == 1 ):
            if( self.sonidito == 0 ):
                self.Lvl4.play()
                self.sonidito = 1

        if( (160 - time.clock()) < 150 ):
            if( self.activate == 0 ):
                self.activate = 1
                self.perdio = 0"""
            
        
        if( self.Perdio == 0 ):
            global tempo
            tempo.destroy()
            #tiempito = "%.2f" % (time.clock())
            tiempito2 = 120 - time.clock()
            tiempito = "%.2f" % (tiempito2)
            tempo = addText( 0.9, 0.3,  "Tiempo Restante: " + tiempito + " Seg", 0.07 )
            if( tiempito2 <= 0 ):
                self.Perdio = 1
                global text
                text.destroy()
                text = addText(0.01, -0.6,  " GAME OVER ", 0.2)
                global tempo
                tempo.destroy()
                tempo = addText( 0.9, 0.3,  "Tiempo Restante: 0.0 Seg", 0.07 )
                self.jeep.stop()
                self.Lvl2.stop()
                self.isMoving = False
            if( self.bebidas >= 30 ):
                self.Perdio = 1
                global text
                text.destroy()
                text = addText(0.01, -0.9,  " CONGRATULATIONS ", 0.2)
                self.jeep.stop()
                self.Lvl2.stop()
                self.isMoving = False
            
        #print self.jeep.getX()
        return Task.cont
        
    def setk(self, value):
        if( value == 1): self.angleDegrees = self.angleDegrees + 2.0
        else: self.angleDegrees = self.angleDegrees - 2.0

    def setKey(self, key, value):
        self.keyMap[key] = value

        

    """ -------cam-left and cam-right move the camera en circles --------------- """
    """ -----------  follow with the camera to the character ------------------- """

    def move(self, task):

        if( self.Perdio == 0 ):

            if ( (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0)):
                if self.isMoving is False:
                    self.jeep.loop("walk",1)
                    self.isMoving = True
                    self.Lvl2.play()
            else:
                if self.isMoving:
                    self.jeep.stop()
                    self.Lvl2.stop()
                    self.isMoving = False
            
            if( self.keyMap["cam-left"] != 0 ):
                    self.setk(0)
                    angleRadians = self.angleDegrees * ( pi / 180 )
                    base.camera.setPos( 40*sin(angleRadians)+self.jeep.getX(),-40.0 * cos( angleRadians )+self.jeep.getY(), 3)
                    base.camera.setHpr( self.angleDegrees, 0  , 0 )
                    
            if( self.keyMap["cam-right"] != 0 ):
                    self.setk(1)
                    angleRadians = self.angleDegrees * ( pi / 180 )
                    base.camera.setPos( 40*sin(angleRadians)+self.jeep.getX(),-40.0 * cos( angleRadians )+self.jeep.getY(), 3)
                    base.camera.setHpr( self.angleDegrees, 0  , 0 )
                
            if( self.keyMap["left"] != 0 ):
                
                    self.jeep.setH( self.jeep.getH() + 2.0 )
                    if( self.jeep.getH() > 210000.0 ):
                        self.jeep.setH( self.jeep.getH() - 2.0 )
                    else:
                        self.setk(1)
                        angleRadians = self.angleDegrees * ( pi / 180 )
                        base.camera.setPos( 40*sin(angleRadians)+self.jeep.getX(),-40.0 * cos( angleRadians )+self.jeep.getY(), 3)
                        base.camera.setHpr( self.angleDegrees, 0  , 0 )
                
            if( self.keyMap["right"] != 0 ):
                
                    self.jeep.setH( self.jeep.getH() - 2.0 )
                    if( self.jeep.getH() < -150000.0 ):
                        self.jeep.setH(self.jeep.getH() + 2.0 )
                    else:
                        self.setk(0)
                        angleRadians = self.angleDegrees * ( pi / 180 )
                        base.camera.setPos( 40*sin(angleRadians)+self.jeep.getX(),-40.0 * cos( angleRadians )+self.jeep.getY(), 3)
                        base.camera.setHpr( self.angleDegrees, 0  , 0 )
                        
                
            if (self.keyMap["forward"]!=0):

                    self.jeep.setY(self.jeep, -205 * globalClock.getDt())
            
                    if( self.jeep.getX() < -30 or self.jeep.getX() > 25 ):
                        if( self.isCollision == False ):
                            self.punch.play()
                            self.isCollision = True
                        text.destroy()
                        if( self.jeep.getX() < -30 ): text = addText(-0.2, -0.6,  "Hemos Chocado", 0.1)
                        if( self.jeep.getX() > 25  ): text = addText(-0.2, -0.4,  "Procura Tener Mas Cuidado", 0.1)
                        self.jeep.setY(self.jeep, 205 * globalClock.getDt())
                        #imageObject.destroy()
                        #imageObject = OnscreenImage(image = 'myImage.jpg', pos = (-0.5, 0, 0.02), scale=(0.2,0,0.2) )
                        #imageObject.setTransparency(TransparencyAttrib.MAlpha)
                        #text = addText(-0.2, -0.6,  "Hemos Chocado")
                    else:
                        global text
                        text.destroy()
                        self.isCollision = False
                        #global imageObject
                        #imageObject.destroy()
                        base.camera.setY( base.camera, -143.5*( cos( self.jeep.getH() * (pi/180) ) ) * globalClock.getDt() )

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
    
    """ ------------------------------------------------------------------------ """
    """ ------------------------------------------------------------------------ """

    def showMsge(self,task):
        self.inst1 = addText(-0.2, -0.6,  "Ouch")       

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
            
    
    def follow( self, task ):
        print "hola"
 
w = Draw()
run()

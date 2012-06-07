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


def addText(pos1, pos2, msg, scl):
    return OnscreenText(text=msg, style=2, fg=(1,1,1,1),
                        pos=(pos2, pos1), align=TextNode.ALeft, scale = scl)

text = OnscreenText(text = '', pos = (-0.5, 0.02), scale = 0.07)

class MoveMC(DirectObject):

    def __init__(self,jeep):

        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        self.isMoving = False
        self.angleDegrees = 0
        self.jeep = jeep

        self.Lvl1 = base.loader.loadSfx("sonidos/tales.mp3")
        self.Lvl1.setLoop(True)
        self.Lvl1.setVolume(0.5)
        self.Lvl1.play()

        self.Lvl2 = base.loader.loadSfx("sonidos/vel3.wav")
        self.Lvl2.setLoop(True)
        self.Lvl2.setVolume(0.3)

        self.punch = base.loader.loadSfx("sonidos/punch.mp3")
        self.punch.setVolume(1.0)

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

    """ -------cam-left and cam-right move the camera en circles --------------- """
    """ -----------  follow with the camera to the character ------------------- """

    def move(self, task):

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


        return Task.cont
    
    """ ------------------------------------------------------------------------ """
    """ ------------------------------------------------------------------------ """


    def setKey(self, key, value):
        self.keyMap[key] = value


    def setk(self, value):
        if( value == 1): self.angleDegrees = self.angleDegrees + 2.0
        else: self.angleDegrees = self.angleDegrees - 2.0

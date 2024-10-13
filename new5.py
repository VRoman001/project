from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData
from direct.actor.Actor import Actor

config = '''
win=size 1280 720'''
loadPrcFileData('',config)

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.set_background_color(0.1,0.3,0.5,1)
        self.cam.setPos(0,-60,0)

        self.player = Actor("arm/boneTest_textured2.egg",{"anim1":"arm/boneTest-ArmatureAction.egg"})
        #self.player.reparentTo(self.render)
        self.player.loop('anim1')

        m = 0
        for i in range(4):
            a = self.render.attachNewNode('arm'+str(i))
            a.setPos(i*5,0,0)
            self.player.instanceTo(a)
            m += 1

        '''self.n3 = self.render.get_child(2)
        self.n3.set_pos(self.n3.getPos().x,self.n3.getPos().y,10)
        self.n2 = self.render.get_child(3)
        self.n2.set_pos(self.n3.getPos().x,self.n3.getPos().y,-10)
        self.n4 = self.render.get_child(4)
        self.n4.set_pos(self.n2.getPos().x+5,self.n3.getPos().y,0)'''
            

game = Game()
game.run()
    
        

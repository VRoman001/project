from pygame import*

class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


window = display.set_mode((800,600))
picture = transform.scale(image.load(""),(800,600))


player1 = Object("gost1.2.png",100,100,100,80,10)
player2 = Object("gost1.2.png",150,100,100,80,10)

clock = time.Clock()
 
x1,y1 = 100,100

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(picture,(0,0))
    player1.reset()


    display.update()
    clock.tick(60)
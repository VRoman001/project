import pygame
from random import randint
import time

n = 1
n2 = 1
class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.w = w
        self.h = h
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (self.w, self.h)) #разом 55,55 - параметри
        time_for_Attack = time.monotonic()
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.y += self.speed
        if keys[K_d] and self.rect.x < 1100:
            self.rect.x += self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.y -= self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height


        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        
        


        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

image_list = ['Pacman1.png','Pacman2.png']


menu = display.set_mode((1100,700))
display.set_caption('Pacman')
picture2 = transform.scale(image.load("fon1.jpg"),(1100,700))

window = display.set_mode((1100,700))
picture = transform.scale(image.load("fon1.jpg"),(1100,700))

player1 =  Object("Pacman1.png",500,130,45,49,4)
gost =  Object("gost-1.png",500,230,40,49,4) 
gost1 =  Object("gost-2.png",500,330,40,49,4) 
gost2 =  Object("gost-3.png",800,330,40,49,4) 
gost3 =  Object("gost-4.png",200,330,40,49,4) 
time_for_Attack = time.monotonic()

wall1 = Wall(44,66,77,90,100,900,10)
wall2 = Wall(44,66,77,990,100,10,550)
wall3 = Wall(44,66,77,90,650,910,10)
wall4 = Wall(44,66,77,90,100,10,550)
wall5 = Wall(44,66,77,400,200,260,10)
wall6 = Wall(44,66,77,400,550,260,10)
wall7 = Wall(44,66,77,300,100,10,110)
wall8 = Wall(44,66,77,760,100,10,110)
wall9 = Wall(44,66,77,760,550,10,110)
wall10 = Wall(44,66,77,300,550,10,110)
wall11= Wall(44,66,77,195,210,10,120)
wall12= Wall(44,66,77,195,420,10,120)
wall13= Wall(44,66,77,870,210,10,120)
wall14= Wall(44,66,77,870,420,10,120)
wall15= Wall(44,66,77,400,450,260,10)
wall16= Wall(44,66,77,400,300,10,150)
wall17= Wall(44,66,77,650,300,10,150)
wall18= Wall(44,66,77,400,300,50,10)
wall19= Wall(44,66,77,610,300,50,10)
wall20= Wall(44,66,77,300,300,10,150)
wall21= Wall(44,66,77,760,300,10,150)
#wall_red = Wall(255,0,0,90,525,100,10)
walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)
walls.append(wall6)
walls.append(wall7)
walls.append(wall8)
walls.append(wall9)
walls.append(wall10)
walls.append(wall11)
walls.append(wall12)
walls.append(wall13)
walls.append(wall14)
walls.append(wall15)
walls.append(wall16)
walls.append(wall17)
walls.append(wall18)
walls.append(wall19)
walls.append(wall20)
walls.append(wall21)
#walls.append(wall_red)



game = True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    
    window.blit(picture,(0,0))
    gost.reset()
    gost1.reset()
    gost2.reset()
    gost3.reset()
    player1.reset()
    player1.move()
   
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall10.draw_wall()
    wall11.draw_wall()
    wall12.draw_wall()
    wall13.draw_wall()
    wall14.draw_wall()
    wall15.draw_wall()
    wall16.draw_wall()
    wall17.draw_wall()
    wall18.draw_wall()
    wall19.draw_wall()
    wall20.draw_wall()
    wall21.draw_wall()

    if time.monotonic() - time_for_Attack >= 2:
        player1.image = transform.scale(image.load(image_list[0]),(player1.w,player1.h))
        time_for_Attack = time.monotonic()
    if time.monotonic() - time_for_Attack >= 1:
        player1.image = transform.scale(image.load(image_list[1]),(player1.w,player1.h))

    display.update()
   
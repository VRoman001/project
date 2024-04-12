import pygame
from random import randint
import time

time_for_Attack = time.monotonic()
n = 1
n2 = 1
life = 3
point = 0

class Object(pygame.sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.right = True
        self.r = 'right'
        self.left = False
        self.w = w
        self.h = h
        self.m1 = True
        self.m2 = False
        self.m3 = False
        self.m4 = False
        
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = pygame.transform.scale(pygame.image.load(player_image), (self.w, self.h)) #разом 55,55 - параметри
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def gost(self):
        if gost1.rect.x == 330 and gost1.rect.y == 230:
            self.m1 = True
            self.m2 = False
            self.m3 = False
            self.m4 = False
        if gost1.rect.x == 702:
            self.m1 = False
            self.m2 = True
            self.m3 = False
            self.m4 = False
        if gost1.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = True
            self.m4 = False
        if gost1.rect.x == 330 and gost1.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = False
            self.m4 = True
        if self.m1:
            gost1.rect.x += self.speed
            gost1.rect.y += 0
        if self.m2:
            gost1.rect.y += self.speed
            gost1.rect.x += 0
        if self.m3:
            gost1.rect.x -= self.speed
            gost1.rect.y += 0
        if self.m4:
            gost1.rect.y -= self.speed
            gost1.rect.x += 0


    def gost(self):
        if gost1.rect.x == 330 and gost1.rect.y == 230:
            self.m1 = True
            self.m2 = False
            self.m3 = False
            self.m4 = False
        if gost1.rect.x == 702:
            self.m1 = False
            self.m2 = True
            self.m3 = False
            self.m4 = False
        if gost1.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = True
            self.m4 = False
        if gost1.rect.x == 330 and gost1.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = False
            self.m4 = True
        if self.m1:
            gost1.rect.x += self.speed
            gost1.rect.y += 0
        if self.m2:
            gost1.rect.y += self.speed
            gost1.rect.x += 0
        if self.m3:
            gost1.rect.x -= self.speed
            gost1.rect.y += 0
        if self.m4:
            gost1.rect.y -= self.speed
            gost1.rect.x += 0

    def gost_1(self):
        if gost3.rect.x == 800 and gost3.rect.y == 130:
            self.m1 = True
            self.m2 = False
            self.m3 = False
            self.m4 = False
        if gost3.rect.x == 920:
            self.m1 = False
            self.m2 = True
            self.m3 = False
            self.m4 = False
        if gost3.rect.y == 570:
            self.m1 = False
            self.m2 = False
            self.m3 = True
            self.m4 = False
        if gost3.rect.x == 800 and gost3.rect.y == 570:
            self.m1 = False
            self.m2 = False
            self.m3 = False
            self.m4 = True
        if self.m1:
            gost3.rect.x += self.speed
            gost3.rect.y += 0
        if self.m2:
            gost3.rect.y += self.speed
            gost3.rect.x += 0
        if self.m3:
            gost3.rect.x -= self.speed
            gost3.rect.y += 0
        if self.m4:
            gost3.rect.y -= self.speed
            gost3.rect.x += 0
    
    def gost_2(self):
        if gost4.rect.x == 130 and gost4.rect.y == 130:
            self.m1 = True
            self.m2 = False
            self.m3 = False
            self.m4 = False
        if gost4.rect.x == 230:
            self.m1 = False
            self.m2 = True
            self.m3 = False
            self.m4 = False
        if gost4.rect.y == 570:
            self.m1 = False
            self.m2 = False
            self.m3 = True
            self.m4 = False
        if gost4.rect.x == 130 and gost4.rect.y == 570:
            self.m1 = False
            self.m2 = False
            self.m3 = False
            self.m4 = True
        if self.m1:
            gost4.rect.x += self.speed
            gost4.rect.y += 0
        if self.m2:
            gost4.rect.y += self.speed
            gost4.rect.x += 0
        if self.m3:
            gost4.rect.x -= self.speed
            gost4.rect.y += 0
        if self.m4:
            gost4.rect.y -= self.speed
            gost4.rect.x += 0

    def gost_3(self):
        if gost2.rect.x == 220 and gost2.rect.y == 230:
            self.m1 = True
            self.m2 = False
            self.m3 = False
            self.m4 = False
        if gost2.rect.x == 800:
            self.m1 = False
            self.m2 = True
            self.m3 = False
            self.m4 = False
        if gost2.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = True
            self.m4 = False
        if gost2.rect.x == 220 and gost2.rect.y == 482:
            self.m1 = False
            self.m2 = False
            self.m3 = False
            self.m4 = True
        if self.m1:
            gost2.rect.x += self.speed
            gost2.rect.y += 0
        if self.m2:
            gost2.rect.y += self.speed
            gost2.rect.x += 0
        if self.m3:
            gost2.rect.x -= self.speed
            gost2.rect.y += 0
        if self.m4:
            gost2.rect.y -= self.speed
            gost2.rect.x += 0

    def move(self):
        global time_for_Attack
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.right = False
            self.left = True
            for w in walls:
                if pygame.sprite.collide_rect(player1,w):
                    self.rect.x += self.speed

        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            for w in walls:
                if pygame.sprite.collide_rect(player1,w):
                    self.rect.y += self.speed
        if keys[pygame.K_d] and self.rect.x < 1100:           
            self.rect.x += self.speed
            self.right = True
            self.left = False
            for w in walls:
                if pygame.sprite.collide_rect(player1,w):
                    self.rect.x -= self.speed
        if keys[pygame.K_s] and self.rect.y < 700:
            self.rect.y += self.speed
            for w in walls:
                if pygame.sprite.collide_rect(player1,w):
                    self.rect.y -= self.speed
        if self.right:
            if time.monotonic() - time_for_Attack >= 2:
                self.image = pygame.transform.scale(pygame.image.load(image_list[0]),(self.w,self.h))
                time_for_Attack = time.monotonic()
            if time.monotonic() - time_for_Attack >= 1:
                self.image = pygame.transform.scale(pygame.image.load(image_list[1]),(self.w,self.h))
        if self.left:
            if time.monotonic() - time_for_Attack >= 2:
                self.image = pygame.transform.scale(pygame.image.load(image_list2[0]),(self.w,self.h))
                time_for_Attack = time.monotonic()
            if time.monotonic() - time_for_Attack >= 1:
                self.image = pygame.transform.scale(pygame.image.load(image_list2[1]),(self.w,self.h))
class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height


        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        
        


        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

image_list = ['Pacman1.png','Pacman2.png']
image_list2 = ['Pacman1.1.png','Pacman2.2.png']

menu = pygame.display.set_mode((1100,700))
pygame.display.set_caption('Pacman')
picture2 = pygame.transform.scale(pygame.image.load("fon1.jpg"),(1100,700))

window = pygame.display.set_mode((1100,700))
picture = pygame.transform.scale(pygame.image.load("fon1.jpg"),(1100,700))


player1 =  Object("Pacman1.png",500,130,45,49,3)
gost1 =  Object("gost-1.png",330,230,40,49,4) 
gost2 =  Object("gost-2.png",500,330,40,49,4) 
gost3 =  Object("gost-3.png",800,130,40,49,4) 
gost4 =  Object("gost-4.png",130,130,40,49,4) 

Bust1 = Object("ball_1.png",915,360,20,20,4) 
Bust2 = Object("ball_1.png",140,360,20,20,4) 


coin1  =   Object("ball.png",150,150,10,10,4) 
coin2  =   Object("ball.png",250,150,10,10,4) 
coin3  =   Object("ball.png",150,250,10,10,4) 
coin4  =    Object("ball.png",250,250,10,10,4) 
coin5  =   Object("ball.png",250,370,10,10,4) 
coin6  =   Object("ball.png",250,490,10,10,4) 
coin7  =   Object("ball.png",250,590,10,10,4) 
coin8  =   Object("ball.png",150,490,10,10,4) 
coin9  =   Object("ball.png",150,590,10,10,4)

coin10 =   Object("ball.png",820,150,10,10,4) 
coin11 =   Object("ball.png",920,150,10,10,4) 
coin12 =   Object("ball.png",820,250,10,10,4) 
coin13 =   Object("ball.png",920,250,10,10,4) 
coin14 =   Object("ball.png",820,370,10,10,4) 
coin15 =   Object("ball.png",820,490,10,10,4) 
coin16 =   Object("ball.png",820,590,10,10,4) 
coin17 =   Object("ball.png",920,490,10,10,4) 
coin18 =   Object("ball.png",920,590,10,10,4) 

coin19 =   Object("ball.png",350,250,10,10,4) 
coin20 =   Object("ball.png",350,370,10,10,4) 
coin21 =   Object("ball.png",350,490,10,10,4) 
coin22 =   Object("ball.png",700,250,10,10,4) 
coin23 =   Object("ball.png",700,370,10,10,4) 
coin24 =   Object("ball.png",700,490,10,10,4) 
coin25 =   Object("ball.png",470,250,10,10,4) 
coin26 =   Object("ball.png",580,250,10,10,4) 
coin27 =   Object("ball.png",470,490,10,10,4) 
coin28 =   Object("ball.png",580,490,10,10,4)
coin29 =   Object("ball.png",350,590,10,10,4)
coin30 =   Object("ball.png",470,590,10,10,4)
coin31 =   Object("ball.png",580,590,10,10,4)
coin32 =   Object("ball.png",700,590,10,10,4)
coin33 =   Object("ball.png",350,150,10,10,4)
coin34 =   Object("ball.png",700,150,10,10,4)

coins = []
coins.append(coin1)
coins.append(coin2)
coins.append(coin3)
coins.append(coin4)
coins.append(coin5)
coins.append(coin6)
coins.append(coin7)
coins.append(coin8)
coins.append(coin9)
coins.append(coin10)
coins.append(coin11)
coins.append(coin12)
coins.append(coin13)
coins.append(coin14)
coins.append(coin15)
coins.append(coin16)
coins.append(coin17)
coins.append(coin18)
coins.append(coin19)
coins.append(coin20)
coins.append(coin21)
coins.append(coin22)
coins.append(coin23)
coins.append(coin24)
coins.append(coin25)
coins.append(coin26)
coins.append(coin27)
coins.append(coin28)
coins.append(coin29)
coins.append(coin30)
coins.append(coin31)
coins.append(coin32)
coins.append(coin33)
coins.append(coin34)

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
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False


    
    window.blit(picture,(0,0))

    Bust1.reset()
    Bust2.reset()

    coin1.reset()
    coin2.reset()
    coin3.reset()
    coin4.reset()
    coin5.reset()
    coin6.reset()
    coin7.reset()
    coin8.reset()
    coin9.reset()
    coin10.reset()
    coin11.reset()
    coin12.reset()
    coin13.reset()
    coin14.reset()
    coin15.reset()
    coin16.reset()
    coin17.reset()
    coin18.reset()
    coin19.reset()
    coin20.reset()
    coin21.reset()
    coin22.reset()
    coin23.reset()
    coin24.reset()
    coin25.reset()
    coin26.reset()
    coin27.reset()
    coin28.reset()
    coin29.reset()
    coin30.reset()
    coin31.reset()
    coin32.reset()
    coin33.reset()
    coin34.reset()
    




    gost1.reset()
    gost2.reset()
    gost3.reset()
    gost4.reset()
    player1.reset()
    player1.move()
    gost1.gost()
    gost2.gost_3()
    gost3.gost_1()
    gost4.gost_2()
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

    if pygame.sprite.collide_rect(player1,gost1) or pygame.sprite.collide_rect(player1,gost2) or pygame.sprite.collide_rect(player1,gost3) or pygame.sprite.collide_rect(player1,gost4):
            life -= 1
            player1.rect.x = 500
            player1.rect.y = 130

    for i in coins:
        if i.rect.colliderect(player1.rect):
            i.rect.x = 10000
            point += 1
    
    if point == 34:
        game = False

    if life == 0:
        game = False

    pygame.display.update()
    pygame.time.delay(20)
   
from pygame import*
from random import randint

n = 1
n2 = 1
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
        if keys[K_d] and self.rect.x < 1020:
            self.rect.x += self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < 660:
            self.rect.y += self.speed
            for w in walls:
                if sprite.collide_rect(player1,w):
                    self.rect.y -= self.speed
    r = 'right'
    def move_enemy(self):
        if self.rect.y <= 220:
            self.r = "right"
        elif self.rect.y >= 470:
            self.r = "left"  
        if self.r == 'right':
            self.rect.y += self.speed
        if self.r == 'left':
            self.rect.y -= self.speed  

    def move_enemy_1(self):
        if self.rect.y <= 260:
            self.r = "right"
        elif self.rect.y >= 420:
            self.r = "left"  
        if self.r == 'right':
            self.rect.y += self.speed
        if self.r == 'left':
            self.rect.y -= self.speed 



    def move_enemy_2(self):
        if self.rect.x <= 270:
            self.r = "right"
        elif self.rect.x >= 420:
            self.r = "left"  
        if self.r == 'right':
            self.rect.x += self.speed
        if self.r == 'left':
            self.rect.x -= self.speed

    def move_enemy_3(self):
        if self.rect.y <= 460:
            self.r = "right"
        elif self.rect.y >= 580:
            self.r = "left"  
        if self.r == 'right':
            self.rect.y += self.speed
        if self.r == 'left':
            self.rect.y -= self.speed

    def move_enemy_4(self):
        if self.rect.y <= 100:
            self.r = "right"
        elif self.rect.y >= 470:
            self.r = "left"  
        if self.r == 'right':
            self.rect.y += self.speed
        if self.r == 'left':
            self.rect.y -= self.speed  
        
    def move_enemy_5(self):
        if self.rect.y <= 100:
            self.r = "right"
        elif self.rect.y >= 200:
            self.r = "left"  
        if self.r == 'right':
            self.rect.y += self.speed
        if self.r == 'left':
            self.rect.y -= self.speed  

    def move_enemy_6(self):
        if self.rect.x <= 750:
            self.r = "right"
        elif self.rect.x >= 930:
            self.r = "left"  
        if self.r == 'right':
            self.rect.x += self.speed
        if self.r == 'left':
            self.rect.x -= self.speed         



    def fire(self):
        global n
        n += 1
        if n % 87 == 0:
            arrow = Arrow('arrow3.png',self.rect.centerx,self.rect.centery-5,50,10,10)
            arrows.add(arrow)

    def fire2(self):
        global n2
        n2 += 1
        if n2 % 87 == 0:
            arrow = Arrow2('arrow2.2.png',self.rect.centerx-5,self.rect.centery,10,50,10)
            arrows.add(arrow)

    def fire3(self):
        global n2
        n2 += 1
        if n2 % 87 == 0:
            arrow = Arrow3('arrow2.2.png',self.rect.centerx-5,self.rect.centery,10,50,10)
            arrows.add(arrow)

    def fire4(self):
        global n2
        n2 += 1
        if n2 % 87 == 0:
            arrow = Arrow4('arrow2.2.png',self.rect.centerx-5,self.rect.centery,10,50,10)
            arrows.add(arrow)


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




class Arrow(Object):
    def update(self):
        self.rect.x += 5
        if self.rect.x >= 970:
            self.kill()
        

class Arrow2(Object):
    def update(self):
        self.rect.y += 5
        if self.rect.y >= 170:
                self.kill()


class Arrow3(Object):
    def update(self):
        self.rect.y += 5
        if self.rect.y >= 600:
                self.kill()
    

class Arrow4(Object):
    def update(self):
        self.rect.y += 5
        if self.rect.y >= 490:
                self.kill()

arrows = sprite.Group()
arrows2 = sprite.Group()


menu = display.set_mode((1100,700))
display.set_caption('Лабіринт')
picture2 = transform.scale(image.load("fon1.jpg"),(1100,700))


start_button = Rect(400,180,300,100)
exit_button = Rect(400,300,300,100)

font.init()
menu_font = font.Font(None,48)

mg = True
while mg:
    for e in event.get():
        if e.type == QUIT:
            mg = False
            game = False
        elif e.type == MOUSEBUTTONDOWN and e.button ==1:
            if exit_button.collidepoint(mouse.get_pos()):
                mg = False
                game = False
            elif start_button.collidepoint(mouse.get_pos()):
                mg = False
                game = True
    menu.blit(picture2,(0,0))
    draw.rect(menu,(70,70,70),start_button)
    draw.rect(menu,(70,70,70),exit_button)

    start_text = menu_font.render('Start', True,(0,0,0))
    exit_text = menu_font.render('Exit', True,(0,0,0))
    menu.blit(start_text,(start_button.x+110, start_button.y+30))
    menu.blit(exit_text,(exit_button.x+110, exit_button.y+30))



    display.update()


display.quit()
display.init()


window = display.set_mode((1100,700))
picture = transform.scale(image.load("fon1.jpg"),(1100,700))

keyr = Object("red1.png",819,240,40,40,10)
keyb = Object("blue1.png",510,360,40,40,10)
portal = Object("portal3.png",870,560,100,100,1)
kubok = Object("kubok.png",370,300,100,100,1) 
player1 = Object("gost7.png",50,580,45,49,4)
player2 = Object("gost2-2.png",200,180,70,70,5)

arrow  = Arrow("dispenser.png",795,330,50,30,4)
arrow1 = Arrow("dispenser.png",795,380,50,30,4)
arrow2 = Arrow("dispenser1.png",245,85,30,50,4)
arrow3 = Arrow("dispenser1.png",385,85,30,50,4)
arrow4 = Arrow("dispenser1.png",520,85,30,50,4)
arrow5 = Arrow("dispenser1.png",655,85,30,50,4)
arrow6 = Arrow("dispenser1.png",805,85,30,50,4)
arrow7 = Arrow("dispenser1.png",835,510,30,50,4)
arrow8 = Arrow("dispenser1.png",400,410,30,50,4)


wall1 = Wall(44,66,77,90,100,900,10)
wall2 = Wall(44,66,77,990,100,10,550)
wall3 = Wall(44,66,77,90,650,910,10)
wall4 = Wall(44,66,77,90,100,10,425)
wall5 = Wall(44,66,77,190,200,10,325)
wall6 = Wall(44,66,77,190,525,400,10)
wall7 = Wall(44,66,77,590,325,10,100)
wall8 = Wall(44,66,77,290,325,300,10)
wall9 = Wall(44,66,77,290,425,310,10)
wall10 = Wall(44,66,77,190,200,520,10)
wall11= Wall(44,66,77,710,200,10,120)
wall12= Wall(44,66,77,600,425,220,10)
wall13= Wall(44,66,77,810,310,10,120)
wall14= Wall(44,66,77,810,310,80,10)
wall15= Wall(44,66,77,890,210,10,110)
wall16= Wall(44,66,77,700,200,200,10)
wall17= Wall(44,66,77,710,430,10,220)
wall18= Wall(44,66,77,820,525,170,10)
wall_red = Wall(255,0,0,90,525,100,10)
wall_blue = Wall(44,66,255,710,320,10,110)
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
walls.append(wall_red)
walls.append(wall_blue)



clock = time.Clock()



lvl1 = True
lvl2 = False
while game:
    if lvl1:
        for e in event.get():
            if e.type == QUIT:
                game = False
            #elif e.type == KEYDOWN:
                #if e.key == K_SPACE:
                    #player1.fire()

        window.blit(picture,(0,0))

        arrows.update()
        arrows.draw(window)
        arrows2.update()
        arrows2.draw(window)
        player1.reset()
        player1.move()
        player2.reset()
        player2.move_enemy()
        portal.reset()
        keyr.reset()
        keyb.reset()
        arrow.reset()
        arrow1.reset()
        arrow2.reset()
        arrow3.reset()
        arrow4.reset()
        arrow5.reset()
        arrow6.reset()
        arrow7.reset()
        arrow8.reset()
        arrow.fire()
        arrow1.fire()
        arrow2.fire2()
        arrow3.fire2()
        arrow4.fire2()
        arrow5.fire2()
        arrow6.fire2()
        arrow7.fire3()
        arrow8.fire4()
        



        #відображення стін
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
        wall_red.draw_wall()
        wall_blue.draw_wall()
        

        if sprite.collide_rect(player1,player2):
            game = False
            mg = True
        
        if sprite.spritecollide(player1,arrows,False) or sprite.spritecollide(player1,arrows2,False):
            game = False
            mg = True


        if sprite.collide_rect(player1,keyr):
            keyr.rect.x = -4732
            wall_red.rect.x = -4732

        if sprite.collide_rect(player1,keyb):
            keyb.rect.x = -4732
            wall_blue.rect.x = -4732
#################################### 
        if sprite.collide_rect(player1,portal):
            lvl1 = False
            lvl2 = True
            arrows = sprite.Group()
            arrows2 = sprite.Group()

            window = display.set_mode((1100,700))
            picture = transform.scale(image.load("fon1.jpg"),(1100,700))

            keyr = Object("red1.png",630,350,40,40,10)
            scarb = Object('scarb.png',20,600,40,40,0)
            player1 = Object("gost7.png",150,580,45,45,4)
            player2_2 = Object("gost2-2.png",200,100,70,70,4)
            player3 = Object("gost2-2.png",450,300,70,70,4)
            player4 = Object("gost2-2.png",350,430,70,70,4)
            player5 = Object("gost2-2.png",470,500,70,70,2)
            player6 = Object("gost2-2.png",700,500,70,70,2)
            player7 = Object("gost2-2.png",100,470,70,70,4)
            player8 = Object("gost2-2.png",280,100,70,70,2)
            player9 = Object("gost2-2.png",480,100,70,70,2)
            player10 = Object("gost2-2.png",700,100,70,70,2)
            player11 = Object("gost2-2.png",750,420,70,70,2)
            player12 = Object("gost2-2.png",900,250,70,70,2)
            player13 = Object("gost2-2.png",200,180,70,70,4)


            wall1 = Wall(44,66,77,90,100,900,10)
            wall2 = Wall(44,66,77,990,100,10,550)
            wall3 = Wall(44,66,77,90,650,910,10)
            wall4 = Wall(44,66,77,90,100,10,425)
            wall5 = Wall(44,66,77,270,270,10,385)
            wall6 = Wall(44,66,77,270,265,490,10)
            wall7 = Wall(44,66,77,750,265,10,200)
            wall8 = Wall(44,66,77,470,465,290,10)
            wall9 = Wall(44,66,77,0,650,90,10)
            wall10 = Wall(44,66,77,0,525,90,10)
            wall_red = Wall(255,0,0,90,525,10,125)

            walls = []
            walls.append(wall1)
            walls.append(wall2)
            walls.append(wall3)
            walls.append(wall4)
            walls.append(wall5)
            walls.append(wall6)
            walls.append(wall7)
            walls.append(wall_red)




    if lvl2:
        for e in event.get():
            if e.type == QUIT:
                game = False
            #elif e.type == KEYDOWN:
                #if e.key == K_SPACE:
                    #player1.fire()

        window.blit(picture,(0,0))
        player1.reset()
        player1.move()
        player2_2.reset()
        player2_2.move_enemy_4()
        player3.reset()
        player3.move_enemy_1()
        player4.reset()
        player4.move_enemy_2()
        player5.reset()
        player5.move_enemy_3()
        player6.reset()
        player6.move_enemy_3()
        player7.reset()
        player7.move_enemy_4()
        player8.reset()
        player8.move_enemy_5()
        player9.reset()
        player9.move_enemy_5()       
        player10.reset()
        player10.move_enemy_5()
        player11.reset()
        player11.move_enemy_6()
        player12.reset()
        player12.move_enemy_6() 
        scarb.reset()       
        keyr.reset()

        



        #відображення стін
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
        wall_red.draw_wall()

        

        if sprite.collide_rect(player1,player2_2) or sprite.collide_rect(player1,player3) or sprite.collide_rect(player1,player4) or sprite.collide_rect(player1,player5) or sprite.collide_rect(player1,player6) or sprite.collide_rect(player1,player7) or sprite.collide_rect(player1,player8) or sprite.collide_rect(player1,player9) or sprite.collide_rect(player1,player10) or sprite.collide_rect(player1,player11) or sprite.collide_rect(player1,player12) or sprite.collide_rect(player1,player13) :
            player1.rect.x = 150
            player1.rect.y = 580
            wall_red.rect.x = 90
            keyr.rect.x = 630
            keyr.rect.y = 350


        if sprite.spritecollide(player1,arrows,False) or sprite.spritecollide(player1,arrows2,False):
            game = False
            mg = True


        if sprite.collide_rect(player1,keyr):
            keyr.rect.x = -4732
            wall_red.rect.x = -4732

        if sprite.collide_rect(player1,keyb):
            keyb.rect.x = -4732
            wall_blue.rect.x = -4732

        if sprite.collide_rect(player1,scarb):
            kubok.reset()
            


    display.update()
    clock.tick(60)
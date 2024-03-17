from pygame import*
from project1 import *
import  random 
font.init()
mixer.init()
'''
music.loud('ogg')
mixer.music.play()
sound = mixer.Sound('sound.mp3)
sound.play()
'''

# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        self.height = height
        self.wight = wight
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 
 


#ігрова сцена:
back = (20, 255, 25)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
font2 = font.Font(None,50)
font1 = font.Font(None,70)
racket = Player('racket.png',100,100,5,30,70)
ball = Player('ball.png',300,100,5,20,20)
racket1 = Player('racket.png',500,300,5,30,70)



sc = 0
life = 3
game = True
finish = False
clock = time.Clock()
bx = ball.speed
by = ball.speed
def starting():
    global game
    global finish
    global life
    global bx
    global by
    global clock
    global sc

    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False
    

        f1 = 'Score: ' + str(sc)
        f2 = 'Life: ' + str(life)
        score = font1.render(f1,True,(0,0,0))
        score2 = font2.render(f2,True,(0,0,0))
        window.fill(back)
        window.blit(score,(220,100))
        window.blit(score2,(220,50))

        ball.reset()
        racket.reset()
        racket1.reset()

        racket.update_l()
        
        if ball.rect.y > racket1.rect.y:
            racket1.rect.y += ball.speed
        if ball.rect.y < racket1.rect.y:
            racket1.rect.y -= ball.speed
        
        ball.rect.x += bx
        ball.rect.y += by

        
        if ball.rect.x >= 550 or ball.rect.x <= ball.wight:
            ball.rect.x = 300
            ball.rect.y = random.randint(100,400)
            life -= 1

        if ball.rect.y >= 450 or ball.rect.y <= ball.height:
            by *= -1


        if ball.rect.colliderect(racket) or ball.rect.colliderect(racket1):
            bx *= -1
            bx += 0.01
            by += 0.01

        if ball.rect.colliderect(racket):
            sc += 1
        if life == 0:
            game = False



        display.update()
        clock.tick(60)

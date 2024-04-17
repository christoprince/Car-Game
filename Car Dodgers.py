#importing modules
import pygame,random as r,sys
from pygame.locals import *

#setting up  the window and intializing game variables
pygame.init()
switch='play'

y=0
dodged=0
score=0
car_y=600
game_over=0
speed=17
x=547
size=width,height=(1500,800)
road_wid=width/2
mark_w=width/80

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Car Dodgers (Home Page)")

bg=pygame.image.load('retrobg.jpg')
width = bg.get_rect().width
height = bg.get_rect().height
bg = pygame.transform.scale(bg, (width/2.50, height/2.75))

back=pygame.image.load('back.jpg').convert_alpha()
back= pygame.transform.scale(back, (width/21.5, height/33))

start=pygame.image.load('play.jpg').convert_alpha()
start= pygame.transform.scale(start, (width/15, height/17))

finish=pygame.image.load('exit.jpg').convert_alpha()
finish= pygame.transform.scale(finish, (width/15, height/17))

obs=r.randint(1,4)
obs_x=r.randint(470,1000)


#defining the change of the x position of the player
def player_movement():
    global x
    if switch=='back':
        if event.type ==KEYDOWN:
            if event.key in [K_a, K_LEFT]:#if a or left  key clicked, move left
                if x>460:
                    x-=5
            if event.key in [K_d, K_RIGHT]:#if d or right  key clicked, move right
                if x<1000:
                    x+=5

#checking whether the cars collide
def check_collision():
    global game_over
    if y<741 and y>429 and obs_x<x+70 and obs_x>x-97:
        if game_over==0:
            game_over+=1

#defining the buttons and checking if it is clicked
class Button():
    def __init__(self,x,y,image):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    #drawing the buttons
    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

#displaying the buttons on the window
play=Button(100,200,start)
end=Button(1200,200,finish)
run=True

#the main game code
while run:
    #displaying background
    screen.blit(bg,(0,0))
    
    #checking if the game is over
    if game_over==1:
        y=-200
        car_y=800
        y=0
        dodged=0
        score=0
        car_y=600
        game_over=0
        speed=17
        x=547
        obs=r.randint(1,4)
        obs_x=r.randint(470,1000)

        #changing background
        pygame.display.set_caption("Game Over")
        bg=pygame.image.load('game_over.png')
        width = bg.get_rect().width
        height = bg.get_rect().height
        bg = pygame.transform.scale(bg, (width/2.1, height/2.75))

        #changing button position, purpose and size
        switch='play'
        play=Button(100,200,start)
        finish=pygame.transform.scale(finish,(width/13,height/19))
        end=Button(1200,200,finish)

    #if play button is clicked
    if switch=='back':
        #showing the score 
        font=pygame.font.Font('freesansbold.ttf', 35)
        score_txt=font.render('SCORE: '+str(score),False,('white'))
        dodged_txt=font.render('CARS DODGED: '+str(dodged),False,('white'))
        screen.blit(dodged_txt,(20,150))
        screen.blit(score_txt,(20,100))

        #displaying the players car
        player=pygame.image.load('car.png')
        player=pygame.transform.scale(player,(player.get_rect().width/7,player.get_rect().height/7))
        p_loc=player.get_rect()
        screen.blit(player, (x,car_y))

        #choosing a random car to come from the opposite direction
        if obs==1:
            car2=pygame.image.load('car_1.png')
            car2=pygame.transform.scale(car2,(car2.get_rect().width/6.5,car2.get_rect().height/6.5))
            c2_loc=car2.get_rect()
            screen.blit(car2, (obs_x,y))
        elif obs==2:
            car2=pygame.image.load('car_2.png')
            car2=pygame.transform.scale(car2,(car2.get_rect().width/13,car2.get_rect().height/13))
            c2_loc=car2.get_rect()
            screen.blit(car2, (obs_x,y))
        elif obs==3:
            car2=pygame.image.load('car_3.png')
            car2=pygame.transform.scale(car2,(car2.get_rect().width/13,car2.get_rect().height/13))
            c2_loc=car2.get_rect()
            screen.blit(car2, (obs_x,y))
        elif obs==4:
            car2=pygame.image.load('car_4.png')
            car2=pygame.transform.scale(car2,(car2.get_rect().width/13,car2.get_rect().height/13))
            c2_loc=car2.get_rect()
            screen.blit(car2, (obs_x,y))

        #bringing the car downwards
        if game_over==0:
            y+=speed

            #checking whether car crosses the bottom of the window
            if y>height:
                #changing the scores
                dodged+=1
                score+=5
                #changing opposite car and its position
                y=-200
                obs=r.randint(1,4)
                obs_x=r.randint(470,1000)
                if speed<50:
                    speed+=0.5

        #checking for collision
        check_collision()

    #purpose of the play button
    if play.draw():
        if switch=='play':
            pygame.display.set_caption('Car Dodgers (Game Page)')
            play=Button(15,10,back)
            finish=pygame.transform.scale(finish,(width/18,height/22))
            end=Button(0,700,finish)
            switch='back'

        #purpose of the back button
        else:
            if game_over==0:
                pygame.display.set_caption("Car Dodgers (Home Page)")
            bg=pygame.image.load('retrobg.jpg')
            width = bg.get_rect().width
            height = bg.get_rect().height
            bg = pygame.transform.scale(bg, (width/2.50, height/2.75))
            switch='play'
            play=Button(100,200,start)
            finish=pygame.transform.scale(finish,(width/15,height/17))
            end=Button(1200,200,finish)

    #purpose of the exit button
    if end.draw():
        run=False

    #allowing the pygame window to be closed
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    #changing player position when keys are pressed
    player_movement()

    #changing background when play button is clicked
    if switch=='back':
        bg=pygame.image.load('road.png')
        width = bg.get_rect().width
        height = bg.get_rect().height

    #updating the window
    pygame.display.flip()

#quitting the window
pygame.quit()

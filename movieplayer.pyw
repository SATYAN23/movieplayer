import pygame
from pygame.locals import *
import moviepy
from moviepy import editor
pygame.init()
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height),FULLSCREEN)


antman_image = pygame.image.load("antman.png").convert_alpha()
gravity_image = pygame.image.load("gravity.png").convert_alpha()
interstellar_image = pygame.image.load("interstellar.png").convert_alpha()
the_martian_image = pygame.image.load("the martian.png").convert_alpha()




class button:
    def __init__(self,x,y,image,scale):

        wid = image.get_width()
        hei = image.get_height()
        
        self.image = pygame.transform.scale(image, (int(wid*scale),int(hei*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.clicked= True
                action = True

        if pygame.mouse.get_pressed()[0]==0:
           self.clicked= False 

        screen.blit(self.image, (self.rect.x,self.rect.y))
        return action

gravity_button = button(300,100, gravity_image, 0.7)
antman_button  = button(100,100, antman_image, 0.7)
interstellar_button =  button(100,400, interstellar_image, 0.7)
the_martian_button =  button(300,400, the_martian_image,0.7)
                    
run = True
while run:

    screen.fill((202,228,241))
    if gravity_button.draw():
        video = moviepy.editor.VideoFileClip("gravity.mp4")
        video.preview()  
    if antman_button.draw():
        video = moviepy.editor.VideoFileClip("antman.mp4")
        video.preview()
    if interstellar_button.draw():
        video = moviepy.editor.VideoFileClip("interstellar.mp4")
        video.preview()
    if the_martian_button.draw():
        video = moviepy.editor.VideoFileClip("the martian.mp4")
        video.preview()
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

            


    pygame.display.update()
pygame.quit() 

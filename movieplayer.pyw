import os
import math as m
import pygame
from datetime import datetime
import time
import pyautogui
from pygame.locals import *
width, height = pyautogui.size()
pygame.init()


i_icon = '.\M.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
pygame.init()


i_icon = open(r"C:\Users\nagir\OneDrive\Desktop\rx.png")
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption("movieplayer")


video = moviepy.editor.VideoFileClip("gravitymovie.mp4")
video.preview()
pygame.quit()

def main():
    

    width = 500
    height = 500
    r = 200
    win = pygame.display.set_mode((width, height),RESIZABLE)
    pygame.display.set_caption("movie player")
    font = pygame.font.SysFont("Segoe UI", 16)
    clock = pygame.time.Clock()
    cpt = win.get_rect().center

   

        
        
    run = True
    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        win.fill((255, 255, 255))        
                                          
        pygame.display.update()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()

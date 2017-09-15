#metronomopy.py

from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('metro_bar.wav')

def playSound(filename):
    #pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

while(True):
    sleep(0.5-0.03)
    playSound('metro_bar.wav')
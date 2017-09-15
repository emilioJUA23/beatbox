#import_seccion
from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame

def calcular_figuras(bmp):
    negra = 60.0/bmp
    blanca = 2*negra
    redonda = 4*negra
    corchea = 0.5*negra
    semicorchea = 0.25*negra
    return {
        'semicorchea': semicorchea,
        'corchea': corchea,
        'negra': negra,
        'blanca': blanca,
        'redonda': redonda}

def shutdown():
    check_call(['sudo', 'poweroff'])

#donde x es el numero de gpio que utilizaremos como boton de apagar
def shutdown_button(x):
    shutdown_btn = Button(x, hold_time=2)
    shutdown_btn.when_held = shutdown

def activar_sonido():
    pygame.init()
    pygame.mixer.music.load('metro_bar.wav')

def playSound(filename):
    pygame.mixer.music.play()

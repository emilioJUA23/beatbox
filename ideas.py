#import section
from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame
import funciones
from funciones import calcular_figuras,shutdown_button,playSound

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.music.load('metro_bar.wav')

def nivel_3(led):
    # primer compas
    #1
    playSound()
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)
    # 3
    playSound()
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)

def nivel_2(led):
    # primer compas
    #1
    playSound()
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea']*0.2)
    led.on()
    sleep(f['corchea']*0.8)
    # 4
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)

def nivel_1(led):
    # primer compas
    #1
    playSound()
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # segundo compas
    #1
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    #an
    led.on()
    sleep(f['corchea'])
    # 2
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea'])
    # 4
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # tercer compas
    #1
    playSound()
    led.off()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea'])
    # 3
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # cuarto compas
    #1
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    #an
    led.on()
    sleep(f['corchea'])
    # 2
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea'])
    # quinto compas
    #1
    playSound()
    led.off()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 3
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea'])
    # 4
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # sexto compas
    #1
    playSound()
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 4
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # septimo compas
    #1
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    #an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 2
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea'])
    # 3
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # octavo compas
    #1
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    #an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 2
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 3
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 4
    playSound()
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)


def despedida():
    pass

led1 = LED(17)  #led de prueba para saludo y repite el patron
shutdown_button(2) #define boton de apagado en el gpio
nivel = 1       #define el nivel que vamos a practicar
#tempo = int(input("Enter a tempo: "))    #el tempo en el cual nos vamos a mover
tempo=60
f = calcular_figuras(tempo)
# prosigue el programa
for i in [1,2,3,4,5,6,7,8]:
    playSound()
    sleep(f['negra'])
while True:
    if nivel==1:
        nivel_1(led1)
    elif nivel ==2:
        nivel_2(led1)
    elif nivel == 3:
        nivel_3(led1)
    else:
        pass

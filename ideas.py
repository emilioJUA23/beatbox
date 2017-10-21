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

def encender_led(led):
    led.on()
    sleep(f['corchea'])
    led.off()

def apagar_led(led):
    led.off()
    sleep(f['corchea'])

def nivel_1():
    # primer compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    # 2
    playSound()
    encender_led(led3)
    # an
    apagar_led(led4)
    # 3
    playSound()
    encender_led(led5)
    # an
    apagar_led(led6)
    # 4
    playSound()
    encender_led(led7)
    # an
    apagar_led(led8)
    #segundo compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    apagar_led(led8)
    #tercer compas
    #1
    playSound()
    apagar_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #cuarto compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #quinto compas
    #1
    playSound()
    apagar_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    apagar_led(led8)
    #sexto compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #septimo compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #octavo compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)

def nivel_2(led):
    # primer compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    # 2
    playSound()
    encender_led(led3)
    # an
    apagar_led(led4)
    # 3
    playSound()
    encender_led(led5)
    # an
    encender_led(led6)
    # 4
    playSound()
    apagar_led(led7)
    # an
    encender_led(led8)
    #segundo compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #tercer compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #cuarto compas
    #1
    playSound()
    apagar_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #quinto compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #sexto compas
    #1
    playSound()
    apagar_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    apagar_led(led8)
    #septimo compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    apagar_led(led8)
    #octavo compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)


def nivel_3(led):
    # primer compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    # 2
    playSound()
    encender_led(led3)
    # an
    encender_led(led4)
    # 3
    playSound()
    encender_led(led5)
    # an
    apagar_led(led6)
    # 4
    playSound()
    encender_led(led7)
    # an
    encender_led(led8)
    #segundo compas
    #1
    playSound()
    apagar_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #tercer compas
    #1
    playSound()
    apagar_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #cuarto compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #quinto compas
    #1
    playSound()
    apagar_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #sexto compas
    #1
    playSound()
    encender_led(led1)
    #an
    apagar_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    apagar_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)
    #septimo compas
    #1
    playSound()
    apagar_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    apagar_led(led3)
    #an
    encender_led(led4)
    #3
    playSound()
    apagar_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    encender_led(led7)
    #an
    encender_led(led8)
    #octavo compas
    #1
    playSound()
    encender_led(led1)
    #an
    encender_led(led2)
    #2
    playSound()
    encender_led(led3)
    #an
    apagar_led(led4)
    #3
    playSound()
    encender_led(led5)
    #an
    encender_led(led6)
    #4
    playSound()
    apagar_led(led7)
    #an
    encender_led(led8)


led1,led2,led3,led4,led5,led6,led7,led8 = LED(14),LED(15),LED(18),LED(23),LED(24),LED(25),LED(8),LED(7)  #led de prueba para saludo y repite el patron
shutdown_button(10) #define boton de apagado en el gpio
sonido_mas,sonido_menos,bmp_mas,bmp_menos,pulsado= Button(2),Button(3),Button(4),Button(17),Button(27)
nivel = 1       #define el nivel que vamos a practicar
centinela_reaction= 0 #esta variable cambiara de estado cuando la persona deba de presionar el boton 0 para realse 1 para push

#tempo = int(input("Enter a tempo: "))    #el tempo en el cual nos vamos a mover
tempo=60
f = calcular_figuras(tempo)
# prosigue el programa
for i in range(1,9):
    playSound()
    sleep(f['negra'])
while True:
    if nivel==1:
        nivel_1()
    elif nivel ==2:
        nivel_2(led1)
    elif nivel == 3:
        nivel_3(led1)
    else:
        pass

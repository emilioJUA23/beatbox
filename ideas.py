#import section
from gpiozero import Device, LED
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
    centinela_reaction=1
    sleep(f['corchea'])
    led.off()
    centinela_reaction=0

def apagar_led(led):
    led.off()
    sleep(f['corchea'])


def when_pressed_b():
    if centinela_reaction == 1:
        led_r.off()
        led_v.on()
    else:
        led_r.on()
        led_v.off()


def nivel_1():
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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


def nivel_2():
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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


def nivel_3():
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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
    for a in [1, 2]:
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


def nivel_4():
    for a in [1, 2]:
        # primer compas
        #1
        playSound()
        encender_led(led1)
        #an
        encender_led(led2)
        # 2
        playSound()
        apagar_led(led3)
        # an
        encender_led(led4)
        # 3
        playSound()
        encender_led(led5)
        # an
        apagar_led(led6)
        # 4
        playSound()
        apagar_led(led7)
        # an
        encender_led(led8)
    for a in [1, 2]:
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
        encender_led(led5)
        #an
        encender_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
        #tercer compas
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
        apagar_led(led5)
        #an
        encender_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
        #cuarto compas
        #1
        playSound()
        apagar_led(led1)
        #an
        encender_led(led2)
        #2
        playSound()
        encender_led(led3)
        #an
        apagar_led(led4)
        #3
        playSound()
        enceder_led(led5)
        #an
        apagar_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
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
        apagar_led(led6)
        #4
        playSound()
        encender_led(led7)
        #an
        apagar_led(led8)
    for a in [1, 2]:
        #sexto compas
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
        apagar_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
        #septimo compas
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
        enceder_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
        #octavo compas
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


def nivel_5():
    for a in [1, 2]:
        # primer compas
        #1
        playSound()
        apagar_led(led1)
        #an
        encender_led(led2)
        # 2
        playSound()
        apagar_led(led3)
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
        apagar_led(led8)
    for a in [1, 2]:
        #segundo compas
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
    for a in [1, 2]:
        #tercer compas
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
        encender_led(led7)
        #an
        apagar_led(led8)
    for a in [1, 2]:
        #cuarto compas
        #1
        playSound()
        encender_led(led1)
        #an
        apagar_led(led2)
        #2
        playSound()
        apagar_led(led3)
        #an
        apagar_led(led4)
        #3
        playSound()
        enceder_led(led5)
        #an
        apagar_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)
    for a in [1, 2]:
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
        apagar_led(led6)
        #4
        playSound()
        encender_led(led7)
        #an
        apagar_led(led8)
    for a in [1, 2]:
        #sexto compas
        #1
        playSound()
        apagar_led(led1)
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
        apagar_led(led6)
        #4
        playSound()
        apagar_led(led7)
        #an
        encender_led(led8)

led1,led2,led3,led4,led5,led6,led7,led8 = LED(5),LED(6),LED(12),LED(13),LED(19),LED(16),LED(26),LED(20)  #led de prueba para saludo y repite el patron
#shutdown_button(10) #define boton de apagado en el gpio
#sonido_mas,sonido_menos,bmp_mas,bmp_menos,pulsado= Button(2),Button(3),Button(4),Button(17),Button(27)
nivel = 1       #define el nivel que vamos a practicar
centinela_reaction= 0 #esta variable cambiara de estado cuando la persona deba de presionar el boton 0 para realse 1 para push
led_r, led_v= None,None

#tempo = int(input("Enter a tempo: "))    #el tempo en el cual nos vamos a mover
tempo=60
f = calcular_figuras(tempo)
# prosigue el programa
for i in range(1,9):
    playSound()
    sleep(f['negra'])
while True:
    if nivel == 1:
        nivel_1()
    elif nivel == 2:
        nivel_2()
    elif nivel == 3:
        nivel_3()
    elif nivel == 4:
        nivel_4()
    elif nivel == 5:
        nivel_5()
    else:
        pass

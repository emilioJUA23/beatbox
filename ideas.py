#import section
from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame
from funciones import calcular_figuras,shutdown_button,activar_sonido,playSound

def nivel_3(led):
    # primer compas
    #1
    playSound('metro_bar.wav')
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound('metro_bar.wav')
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)
    # 3
    playSound('metro_bar.wav')
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound('metro_bar.wav')
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea']*0.1)
    led.on()
    sleep(f['corchea']*0.9)

def nivel_2():
    pass

def nivel_1():
    pass

def despedida():
    pass

led1 = LED(27)  #led de prueba para saludo y repite el patron   
shutdown_button(2) #define boton de apagado en el gpio
nivel = 3       #define el nivel que vamos a practicar
tempo = 60.0    #el tempo en el cual nos vamos a mover
f = calcular_figuras(tempo)
# prosigue el programa
while True:
    if nivell==1:
        nivel_1(led1)
    elif nivel ==2:
        nivel_2
    else nivel == 3:
        nivel_3(led1)

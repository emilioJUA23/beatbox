#import section
from gpiozero import LED
from gpiozero import Button
from time import sleep
from funciones import calcular_figuras,shutdown_button,activar_sonido,playSound
import pygame

led1 = LED(27)  #led de prueba para saludo y repite el patron
metronomo=None
nivel = 3
tempo = 60.0


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


f = calcular_figuras(tempo)
led1.off()
playSound('metro_bar.wav')
sleep(f['negra'])
playSound('metro_bar.wav')
sleep(f['negra'])
playSound('metro_bar.wav')
sleep(f['negra'])
playSound('metro_bar.wav')
sleep(f['negra'])
# prosigue el programa
while True:
    if nivell==1:
        nivel_1(led1)
    elif nivel ==2:
        nivel_2
    else nivel == 3:
        nivel_3(led1)

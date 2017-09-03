from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame

pygame.init()
pygame.mixer.music.load('metro_bar.wav')
led1 = LED(27)  #led de prueba para saludo y repite el patron
metronomo=None
nivel = 3
tempo = 60.0

#funcion para apagar la raspberry
def shutdown():
    check_call(['sudo', 'poweroff'])

def playSound(filename):
    #pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

# donde x es el numero de gpio que usaremos en el boton
shutdown_btn = Button(2, hold_time=2)
shutdown_btn.when_held = shutdown


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
    if nivel == 3:
        nivel_3(led1)



from gpiozero import LED
from time import sleep
import pygame

led1 = None  #led de prueba para saludo y repite el patron
metronomo(None)
nivel = 3
tempo = 110

#funcion para apagar la raspberry
def shutdown():
    check_call(['sudo', 'poweroff'])

# donde x es el numero de gpio que usaremos en el boton
shutdown_btn = Button(x, hold_time=2)
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
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    led.on()
    sleep(f['corchea'])
    # an
    led.on()
    sleep(f['corchea'])
    # 3
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    led.on()
    sleep(f['corchea'])
    # an
    led.on()
    sleep(f['corchea'])


saludo = 3  # para poder saludar por 3 segundos al usuario
while saludo > 3:
    led1.on()
    sleep(0.5)
    led1.off()
    sleep(0.5)
    saludo -= 1

f = calcular_figuras(tempo)
led1.off()
sleep(4*f['negra'])
# prosigue el programa
while True:
    if nivel == 1:
        nivel_3(led1)



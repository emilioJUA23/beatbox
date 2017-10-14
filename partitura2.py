#import section
from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame
import funciones
from funciones import calcular_figuras,shutdown_button,playSound
from subprocess import check_call
from signal import pause

def nivel_2(led,f):
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
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # segundo compas
    #1
    playSound()
    led.on()
    sleep(f['corchea'])
    #an
    led.off()
    sleep(f['corchea'])
    # 2
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # 3
    playSound()
    led.on()
    sleep(f['corchea'])
    # an
    led.off()
    sleep(f['corchea'])
    # 4
    playSound()
    led.off()
    sleep(f['corchea'])
    # an
    led.on()
    sleep(f['corchea']*0.8)
    led.off()
    sleep(f['corchea']*0.2)
    # tercer compas
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
    led.off()
    sleep(f['corchea'])
    # 3
    playSound()
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
    led.on()
    sleep(f['corchea'])
    # cuarto compas
    #1
    playSound()
    #an
    # 2
    playSound()
    # an
    # 3
    playSound()
    # an
    # 4
    playSound()
    # an
    # quinto compas
    #1
    playSound()
    #an
    # 2
    playSound()
    # an
    # 3
    playSound()
    # an
    # 4
    playSound()
    # an
    # sexto compas
    #1
    playSound()
    #an
    # 2
    playSound()
    # an
    # 3
    playSound()
    # an
    # 4
    playSound()
    # an
    # septimo compas
    #1
    playSound()
    #an
    # 2
    playSound()
    # an
    # 3
    playSound()
    # an
    # 4
    playSound()
    # an
    # octavo compas
    #1
    playSound()
    #an
    # 2
    playSound()
    # an
    # 3
    playSound()
    # an
    # 4
    playSound()
    # an

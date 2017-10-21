#import section
from gpiozero import LED
from gpiozero import Button
from time import sleep
import pygame
import funciones
from funciones import calcular_figuras,shutdown_button,playSound
from subprocess import check_call
from signal import pause

def nivel_1(led,f):
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

from gpiozero import Device, LED, Button

button1 = Button(5)
button2 = Button(6)
led = None

def say_hello():
    led=LED(5)
    led.on()

button2.when_pressed = say_hello

while True:
    pass
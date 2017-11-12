from gpiozero import Device, LED, Button

button1 = Button(6)
button2 = Button(5)
led = None

def say_hello():
    led=LED(6)
    led.on()

button2.when_pressed = say_hello

while True:
    pass
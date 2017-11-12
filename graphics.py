try:
    from tkinter import *  # python 3
except (SystemError, ValueError, ImportError):
    from Tkinter import *  # python 2
import os
from gpiozero import Device, LED, Button

#primera forma es de nivel
root = Tk()  # create a Tk root window

w = 400  # width for the Tk root
h = 267  # height for the Tk root
nivel = 0
bpm = 60
def makeSomething(value=None, value_bmp=None):
    if value:
        global nivel
        nivel = value
        global root
        root.destroy()
    if value_bmp:
        global bpm
        if value_bmp == "+":
            bpm += 5
        else:
            bpm -= 5
        if bpm > 140:
            bpm = bpm % 60
        elif bpm < 60:
            bpm += 80
        label.config(text=str(bpm))

def bpm_definition(value_bmp,win):
    global bmp
    if value_bmp == "+":
        bmp += 5
    else:
        bmp -= 5
    if bmp > 140:
        bmp = bmp % 60
    elif bmp < 60:
        bmp += 80
    win.update()


# calculate x and y coordinates for the Tk root window
x = 10
y = 10

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
topFrame = Frame(root)
topFrame.pack(side=TOP,fill=BOTH,expand=1)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM,fill=BOTH, expand=1)
button1 = Button(bottomFrame, text="1", command=lambda *args: makeSomething(1))
button1.pack(side=LEFT, fill=BOTH,expand=1)
button2 = Button(bottomFrame, text="2", command=lambda *args: makeSomething(2))
button2.pack(side=LEFT, fill=BOTH,expand=1)
button3 = Button(bottomFrame, text="3", command=lambda *args: makeSomething(3))
button3.pack(side=LEFT, fill=BOTH,expand=1)
button4 = Button(bottomFrame, text="4", command=lambda *args: makeSomething(4))
button4.pack(side=LEFT, fill=BOTH,expand=1)
button5 = Button(bottomFrame, text="5", command=lambda *args: makeSomething(5))
button5.pack(side=LEFT, fill=BOTH,expand=1)
# img = ImageTk.PhotoImage(Image.open("duck.gif"))
# label = Label(topFrame,image= img)
Photo = PhotoImage(file="tux.png")
originalPlantImage = PhotoImage(file="tux.png")
Photo = originalPlantImage.subsample(3, 3)
label = Label(topFrame, image=Photo)
label.pack(expand=1, fill=BOTH)
root.mainloop()  # starts the
print(nivel)
#segunda forma verifica bmp
root = Tk()
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#dividimos el root en izquierda y derecha para label de metronomo izquierda para botones +/-
leftFrame = Frame(root)
leftFrame.pack(side=LEFT, fill=BOTH, expand=1)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, fill=BOTH, expand=1)
mycolor = '#%02x%02x%02x' % (138, 169, 206)
label = Label(rightFrame, text=str(bpm), font="Ostrich 20 bold",fg = mycolor)
label.pack(side=TOP, fill=BOTH, expand=1)
button1 = Button(leftFrame, text="+", command=lambda *args:makeSomething(None, "+"))
button1.pack(side=TOP, fill=BOTH, expand=1)
button2 = Button(leftFrame, text="-",command=lambda *args:makeSomething(None, "-"))
button2.pack(side=TOP, fill=BOTH, expand=1)
root.mainloop()
print(bpm)
les=LED(5)



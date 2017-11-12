try:
    from tkinter import *  # python 3
except (SystemError, ValueError, ImportError):
    from Tkinter import *  # python 2
import os
#primera forma es de nivel
w = 480  # width for the Tk root
h = 290  # height for the Tk root
nivel = 1
bpm = 100
def makeSomething(value=None, value_bmp=None):
    if value:
        global nivel
        if value == "+":
            nivel += 1
        elif value == "-":
            nivel -= 1
        elif value == "des":
            root.destroy()
        if nivel > 5:
            nivel = nivel % 5
        elif nivel < 1:
            nivel += 5
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
root = Tk()  # create a Tk root window
root.geometry('%dx%d+%d+%d' % (w, h+5, x, y))
originalPlantImagelogo = PhotoImage(file="LOGOTIPO.png")
Photologo = originalPlantImagelogo.subsample(3, 3)
label = Label(root, image=Photologo)
label.pack(side=TOP, expand=1, fill=X)
root.after(5000, lambda: root.destroy())
root.mainloop()
root = Tk()  # create a Tk root window
root.geometry('%dx%d+%d+%d' % (w, h+5, x, y))
originalPlantImagelogo = PhotoImage(file="LOGOTIPO.png")
Photologo = originalPlantImagelogo.subsample(3, 3)
label = Label(root, image=Photologo)
label.pack(side=TOP, expand=1, fill=X)
labelpress = Label(root, text="PRESS TO START",font="Ostrich 8 bold")
labelpress.pack(side=TOP, fill=BOTH, expand=1)
root.mainloop()
root = Tk()
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
topFrame = Frame(root)
topFrame.pack(side=TOP,fill=BOTH,expand=1)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM,fill=BOTH, expand=1)
# button1 = Button(bottomFrame, text="+", command=lambda *args: makeSomething("+"))
# button1.pack(side=LEFT, fill=BOTH,expand=1)
# button2 = Button(bottomFrame, text="-", command=lambda *args: makeSomething("-"))
# button2.pack(side=LEFT, fill=BOTH,expand=1)
# button3 = Button(bottomFrame, text="next", command=lambda *args: makeSomething("des"))
# button3.pack(side=LEFT, fill=BOTH,expand=1)
Photo = PhotoImage(file="LEVEL.png")
originalPlantImage = PhotoImage(file="LEVEL.png")
Photo = originalPlantImage.subsample(5, 5)
Photoplus = PhotoImage(file="plus.png")
originalPlantImageplus = PhotoImage(file="plus.png")
Photoplus = originalPlantImageplus.subsample(3, 3)
Photominus = PhotoImage(file="minus.png")
originalPlantImageminus = PhotoImage(file="minus.png")
Photominus = originalPlantImageminus.subsample(3, 3)
label = Label(topFrame, image=Photo)
label.pack(expand=1, fill=BOTH)
label1= Label(bottomFrame, image=Photominus)
label2= Label(bottomFrame, text=str(nivel), font="Ostrich 40 bold")
label3= Label(bottomFrame, image=Photoplus)
label1.pack(side=LEFT, fill=BOTH,expand=1)
label2.pack(side=LEFT, fill=BOTH,expand=1)
label3.pack(side=LEFT, fill=BOTH,expand=1)
root.mainloop()  # starts the
#segunda forma verifica bmp
root = Tk()
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
topFrame = Frame(root)
topFrame.pack(side=TOP,fill=BOTH,expand=1)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM,fill=BOTH, expand=1)
# button1 = Button(bottomFrame, text="+", command=lambda *args: makeSomething("+"))
# button1.pack(side=LEFT, fill=BOTH,expand=1)
# button2 = Button(bottomFrame, text="-", command=lambda *args: makeSomething("-"))
# button2.pack(side=LEFT, fill=BOTH,expand=1)
# button3 = Button(bottomFrame, text="next", command=lambda *args: makeSomething("des"))
# button3.pack(side=LEFT, fill=BOTH,expand=1)
Photo = PhotoImage(file="TEMPO.png")
originalPlantImage = PhotoImage(file="TEMPO.png")
Photo = originalPlantImage.subsample(5, 5)
Photoplus = PhotoImage(file="plus.png")
originalPlantImageplus = PhotoImage(file="plus.png")
Photoplus = originalPlantImageplus.subsample(3, 3)
Photominus = PhotoImage(file="minus.png")
originalPlantImageminus = PhotoImage(file="minus.png")
Photominus = originalPlantImageminus.subsample(3, 3)
label = Label(topFrame, image=Photo)
label.pack(expand=1, fill=BOTH)
label1= Label(bottomFrame, image=Photominus)
label2= Label(bottomFrame, text=str(bpm), font="Ostrich 40 bold")
label3= Label(bottomFrame, image=Photoplus)
label1.pack(side=LEFT, fill=BOTH,expand=1)
label2.pack(side=LEFT, fill=BOTH,expand=1)
label3.pack(side=LEFT, fill=BOTH,expand=1)
root.mainloop()  # starts the
print(nivel)
print(bpm)
mycolor = '#%02x%02x%02x' % (138, 169, 206)

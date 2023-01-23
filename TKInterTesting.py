from tkinter import *


myTk = Tk()
myTk.geometry("300x400")

myCanvas = Canvas(myTk, bd=4, bg="blue", cursor="circle", height=300, width=300)
anything = myCanvas.create_polygon(3,3, 80, 90, 0, 300)
myCanvas.pack()
myCanvas.mainloop()


'''window = Tk()
counter = 1

def clicker():
    labeltester = Label(window, text="It worked!")
    labeltester.grid(row = counter, column = 0)
    pass

theButton = Button(window, text="Click Me!!!", command=clicker(), width=20, height=20)
theButton.grid(row = 0, column = 0, ipadx=100)

window.mainloop()

label1 = tk.Label(window, text="Funny Test")
label2 = tk.Label(window, text="Namey")
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)
window.mainloop()'''
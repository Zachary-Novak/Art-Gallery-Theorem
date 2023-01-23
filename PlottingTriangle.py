from tkinter import *

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=4, bg="ivory", cursor="circle", height=300, width=300)
pointList = []


def draw_dots(event):
    
    x_coord = event.x
    y_coord = event.y
    pointList.append(x_coord)
    pointList.append(y_coord)
    print(len(pointList))
    dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
    if len(pointList) == 4:
        print("We Did IT!")
        anything = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="red")
        pointList.pop(0)
        pointList.pop(0)
        
myCanvas.pack()
myTk.bind("<Button-1>", draw_dots)
myTk.mainloop()

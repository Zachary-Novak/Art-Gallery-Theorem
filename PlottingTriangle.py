from tkinter import *
import math

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height=600, width=1000)
pointList = []
hull = []
finishedHull = False

def insideCircle(point1, point2, point3, point4 = None):
    if point4 == None:
        center = [point1[0] - point2[0], point1[1] - point1[2]]
    pass


def colorInPolygon():
    i = 0
    while i > len(hull):
        
        i = i + 2
    pass

def draw_dots(event):
    global finishedHull
    if not finishedHull:
        x_coord = event.x
        y_coord = event.y
        pointList.append(x_coord)
        pointList.append(y_coord)
        hull.append(x_coord)
        hull.append(y_coord)
        #print(len(pointList))
        if len(hull) > 4 and (math.sqrt(pow((y_coord-hull[1]), 2) + pow((x_coord-hull[0]), 2))) < 5:
            print(len(pointList))
            anything = myCanvas.create_line(pointList[0], pointList[1], hull[0], hull[1], fill="red")
            anything2 = myCanvas.create_polygon
            finishedHull = True
        else:
            dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
            if len(pointList) == 4:
                print("We Did IT!")
                anything = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="red")
                pointList.pop(0)
                pointList.pop(0)

        
myCanvas.pack()
myTk.bind("<Button-1>", draw_dots)
myTk.mainloop()

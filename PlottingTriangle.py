from tkinter import *
import math

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height=600, width=1000)
pointList = []
hull = []
finishedHull = False

def pythagMyBro(point1, point2):
    return math.sqrt(pow(point2[1] - point1[1], 2) + pow(point2[0] - point1[0]))

def insideCircle(circle, point):
    center = circle[0]
    distance = circle[1]
    if pythagMyBro(center, point) < distance:
        return True
    else:
        return False

def findCircle(point1, point2, point3):
    firstLineSlope = (point2[1] - point1[1])/(point2[0]-point2[0])*(-0.5)
    firstLinePoint = [(point2[0] + point1[0])/2, (point2[1]+point1[1])/2]
    
    secondLineSlope = (point3[1] - point1[1])/(point3[0]-point3[0])*(-0.5)
    secondLinePoint = [(point3[0] + point1[0])/2, (point3[1]+point1[1])/2]

    a1 = firstLineSlope
    b1 = 1
    c1 = firstLineSlope*firstLinePoint[0]+firstLinePoint[1]
    
    a2 = secondLinePoint
    b2 = 1
    c2 = secondLineSlope*secondLinePoint[0]+secondLinePoint[1]
    
    circleCenter = [
        (b1*c2-b2*c1)/(a1*b2-a2*b1),
        (a2*c1-a1*c2)/(a1*b2*a2*b1),
    ]
    radius = abs(pythagMyBro(circleCenter, firstLinePoint))
    
    return [circleCenter, radius]
    


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

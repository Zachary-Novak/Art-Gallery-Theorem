from tkinter import *
import math

myTk = Tk()
myTk.title("Triangle Testing")
Canvasx = 1000
Canvasy = 600
myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height=600, width=1000)
pointList = []
hull = []
finishedHull = False
pc = 0
linetype = 2

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

def draw_segment(event):
    global pc
    if pc < 3:
        pc += 1
        x_coord = event.x
        y_coord = event.y
        pointList.append(x_coord)
        pointList.append(y_coord)
        if pc < 3:
            dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
        else:
            dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,fill="yellow",width=0)
        if pc == 2:
            anything = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="red")

def change_line_type(event):
    global linetype
    linetype = (linetype+1)%3
    if linetype == 0:
        myCanvas.create_polygon(pointList[0],pointList[1],pointList[2],pointList[3],pointList[4],pointList[5], fill="yellow", width=0)
        hi = 2
    if linetype == 1:
        r1x = pointList[0]-pointList[4]
        r1y = pointList[1]-pointList[5]
        r2x = pointList[2]-pointList[4]
        r2y = pointList[3]-pointList[5]
        x1set = (r1x > 0)*Canvasx
        x2set = (r2x > 0)*Canvasx
        myCanvas.create_polygon(pointList[4], pointList[5], x1set, pointList[5]+(x1set-pointList[4])*r1y/r1x, x2set, pointList[5]+(x2set-pointList[4])*r2y/r2x, fill="red")
    if linetype == 2:
        v1 = [pointList[4]-pointList[0], pointList[5]-pointList[1]]
        v2 = [pointList[2]-pointList[0], pointList[3]-pointList[1]]
        cosnum = v1[0]*v2[0]+v1[1]*v2[1]
        sinnum = v1[0]*v2[1]-v1[1]*v2[0]
        prodnormsq = (v1[0]*v1[0]+v1[1]*v1[1])*(v2[0]*v2[0]+v2[1]*v2[1])
        rx = ((cosnum*cosnum-sinnum*sinnum)*v1[0]-2*cosnum*sinnum*v1[1])/prodnormsq+pointList[0]
        ry = (2*cosnum*sinnum*v1[0]+(cosnum*cosnum-sinnum*sinnum)*v1[1])/prodnormsq+pointList[1]
        print(rx, ry)
        myCanvas.create_oval(rx-5, ry-5, rx+5, ry+5)
        myCanvas.create_polygon(rx, ry, pointList[0], pointList[1], pointList[2], pointList[3], fill="green")
        
        
myCanvas.pack()
myTk.bind("<Button-1>", draw_segment)
myTk.bind("<space>", change_line_type)
myTk.mainloop()

from asyncio import events
from tkinter import *
import math
import sys
import os

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height=600, width=600)
pointList = []
hull = []
destroyList = []
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

def findIntersection(point1, point2, point3, point4):
        
    try:
        firstLineSlope = (point2[1] - point1[1])/(point2[0]-point1[0])*-1
    except ZeroDivisionError:
        firstLineSlope = float('inf')
    firstLinePoint = point1

    try:
        secondLineSlope = ((point4[1] - point3[1])/(point4[0] - point3[0]))*-1
    except ZeroDivisionError:
        secondLineSlope = float('inf')
    secondLinePoint = point3
    
    
    a1 = firstLineSlope
    b1 = 1
    c1 = firstLineSlope*firstLinePoint[0]+firstLinePoint[1]
    #print("First Slope is: " + str(a1))
    
    a2 = secondLineSlope
    b2 = 1
    c2 = secondLineSlope*secondLinePoint[0]+secondLinePoint[1]
    #print("Second Slope is: " + str(a2))
    #print(str(a1*b2-a2*b1))
    
    if a1 == a2:
        return [float('inf'), float('inf')]
    
    '''if firstLineSlope == float('inf'):
        print("firstlineSlope")
        print(point1)
        print(point2)
        print(point3)
        print(point4)
    if secondLineSlope == float('inf'):
        print("secondLineSlope")
        print(point1)
        print(point2)
        print(point3)
        print(point4)'''
    
    if firstLineSlope == float('inf'):
        intersection = [
            firstLinePoint[0],
            -1*secondLineSlope*firstLinePoint[0]+c2]
        #x_coord = intersection[0]
        #y_coord = intersection[1]
        #dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="black",width=0)
        #print("First Inf")
        #print(intersection)
    elif secondLineSlope == float('inf'):
        intersection = [
            secondLinePoint[0],
            -1*firstLineSlope*secondLinePoint[0]+c1]
        #x_coord = intersection[0]
        #y_coord = intersection[1]
        #dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="black",width=0)
        
        #print("Second Inf")
        #print(intersection)
    elif firstLineSlope != float('inf') and secondLineSlope != float('inf'):
        intersection = [
            -1*(b1*c2-b2*c1)/(a1*b2-a2*b1),
            -1*(a2*c1-a1*c2)/(a1*b2-a2*b1),
        ]
        
        
    else:
        print("Failure :(")
        
    #print(intersection)
    '''if (intersection[0] + 0.000005 > round(intersection[0])):
        intersection[0] = round(intersection[0])   
    if (intersection[0] - 0.000005 < round(intersection[0])):
        intersection[0] = round(intersection[0])
    if (intersection[1] + 0.000005 > round(intersection[1])):
        intersection[1] = round(intersection[1])
    if (intersection[1] - 0.000005 < round(intersection[1])):
        intersection[1] = round(intersection[1])'''
    return intersection

def findCircle(point1, point2, point3):
    circleCenter = findIntersection(point1, point2, point2, point3)
    radius = abs(pythagMyBro(circleCenter, point1))
    
    return [circleCenter, radius]
    
def leftOf(a, b, c):
    area = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if area > 0:
        return False
    else:
        return True

def checkForCross():
    counter = len(hull)-1
    print("counter is " + str(counter))
    print("hull is ")
    print(hull)
    print("\n")
    newPoint = counter
    counter -= 4
    while counter > 2:
        point4 = [hull[counter-3], hull[counter-2]]
        point3 = [hull[counter-1], hull[counter]]
        point2 = [hull[newPoint-3], hull[newPoint-2]]
        point1 = [hull[newPoint-1], hull[newPoint]]
        '''print("\n")
        print(point1)
        print(point2)
        print(point3)
        print(point4)
        print("\n")'''
        
        #print("firstLineSLope: " + str(firstLineSlope))
        
        try:
            secondLineSlope = (point4[1] - point3[1])/(point4[0]-point3[0])
        except ZeroDivisionError:
            secondLineSlope = float('inf')
        #print("secondLineSlope: " + str(secondLineSlope))
        intersection = findIntersection(point1, point2, point3, point4)
        #print("\nIntersection Testing!   Points: " + str((counter/2)+0.5) + " " + str((counter/2)-0.5))
        #print(str(point1[0]) + " " + str(point2[0]) + " " + str(intersection[0]) + " " + str(min([point1[0], point2[0], intersection[0]])))
        #print(str(point1[1]) + " " + str(point2[1]) + " " + str(intersection[1]) + " " + str(min([point1[1], point2[1], intersection[1]])))
        #print(str(point3[0]) + " " + str(point4[0]) + " " + str(intersection[0]) + " " + str(min([point3[0], point4[0], intersection[0]])))
        #print(str(point3[1]) + " " + str(point4[1]) + " " + str(intersection[1]) + " " + str(min([point3[1], point4[1], intersection[1]])))
        #print("\n")
        if (intersection != [float('inf'), float('inf')]):
            print("First Passed")
            if (min([point1[0], point2[0], intersection[0]]) != intersection[0] and max([point1[0], point2[0], intersection[0]]) != intersection[0]) or (intersection[0] == point1[0] and intersection[0] == point2[0]):# and (intersection[1] != point1[1] and intersection[1] != point2[1])):
                print("Second Passed")
                if (min([point1[1], point2[1], intersection[1]]) != intersection[1] and max([point1[1], point2[1], intersection[1]]) != intersection[1]) or (intersection[1] == point1[1] and intersection[1] == point2[1]):# and (intersection[0] != point1[0] and intersection[0] != point2[0])):
                    print("Third Passed")
                    if (min([point3[0], point4[0], intersection[0]]) != intersection[0] and max([point3[0], point4[0], intersection[0]]) != intersection[0]) or (intersection[0] == point3[0] and intersection[0] == point4[0]):# and (intersection[1] != point3[1] and intersection[1] != point4[1])):
                        print("Fourth Passed")
                        if (min([point3[1], point4[1], intersection[1]]) != intersection[1] and max([point3[1], point4[1], intersection[1]]) != intersection[1])  or (intersection[1] == point3[1] and intersection[1] == point4[1]):# and (intersection[0] != point3[0] and intersection[0] != point4[0])):
                            print("\nIntersection Testing!   Points: " + str((counter/2)+0.5) + " " + str((counter/2)-0.5))
                            print(point1)
                            print(point2)
                            print(point3)
                            print(point4)
                            print(intersection)
                            return True
        '''if (intersection != [float('inf'), float('inf')] and 
            ((intersection[1] == point1[1] or intersection[1] == point2[1]) and 
                (min([point1[0], point2[0], intersection[0]]) != intersection[0] and max([point1[0], point2[0], intersection[0]]) != intersection[0])) or
            ((intersection[0] == point1[0] or intersection[0] == point2[0]))
        )'''
        
        counter -= 2
    return False

def colorInPolygon():
    i = 0
    while i > len(hull):
        
        i = i + 2
    pass

def findEdgeDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[0])**2)

def findMidPoint(point1, point2):
    list = []
    list.append((point1[0] + point2[0]) / 2)
    list.append((point1[1] + point2[1]) / 2)
    return list 

def findSlope(point1, point2):
    return (point2[1] - point1[1]) / (point2[0] - point1[0])

"""def createCircle(point1, point2, point3):
   e1 = findEdgeDistance(point1, point2)
   e2 = findEdgeDistance(point2, point3)
   e3 = findEdgeDistance(point1, point3)
   intersecting_point = findIntersection(point1, point2, point1, point2)
   mid_pt = findMidPoint(point1, point2)
   radius = findEdgeDistance(mid_pt, intersecting_point)"""
    
    

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
        if len(destroyList) > 0:
            counter = len(destroyList)-1
            while counter >= 0:
                myCanvas.delete(destroyList[counter])
                counter -= 1
            destroyList.clear()
        if len(hull) > 4 and (math.sqrt(pow((y_coord-hull[1]), 2) + pow((x_coord-hull[0]), 2))) < 5:
            #print(len(pointList))
            anything = myCanvas.create_line(pointList[0], pointList[1], hull[0], hull[1], fill="blue")
            anything2 = myCanvas.create_polygon
            finishedHull = True
        else:
            if len(pointList) == 2:
                dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
            elif len(pointList) == 4 and not checkForCross():
                counter = len(hull)-1
                #if counter > 5:
                    #print("CheckForCross: " + str(checkForCross()))
                dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
                #print("We Did IT!")
                anything = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="blue")
                pointList.pop(0)
                pointList.pop(0)
            else:
                circleBreak = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="red",width=0, tags="DestroyCircle")
                lineBreak = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="black", tags="DestroyLine")
                destroyList.append(circleBreak)
                destroyList.append(lineBreak)
                hull.pop()
                hull.pop()
                pointList.pop()
                pointList.pop()
                
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def FindTriangulation():
    pass
   
myTk.bind("<Button-1>", draw_dots)

quit_button = Button(myTk, text="Exit")
quit_button.pack(side="bottom")
quit_button["command"] = myTk.destroy
restart_button = Button(myTk, text="Restart")
restart_button.pack(side="bottom")
restart_button["command"] = restart_program

myCanvas.pack()

myTk.mainloop()

'''point1 = [300, 300]
point2 = [310, 400]

point3 = [200, 350]
point4 = [400, 350]

print(findIntersection(point1, point2, point3, point4))'''
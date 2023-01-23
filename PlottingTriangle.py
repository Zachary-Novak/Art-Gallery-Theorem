from tkinter import *
import math

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height=600, width=600)
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

def findIntersection(point1, point2, point3, point4):
        
    firstLineSlope = ((point2[1] - point1[1])/(point2[0] - point1[0]))*-1
    firstLinePoint = point1

    secondLineSlope = ((point4[1] - point3[1])/(point4[0] - point3[0]))*-1
    secondLinePoint = point3
    
    a1 = firstLineSlope
    b1 = 1
    c1 = firstLineSlope*firstLinePoint[0]+firstLinePoint[1]
    print("First Slope is: " + str(a1))
    
    a2 = secondLineSlope
    b2 = 1
    c2 = secondLineSlope*secondLinePoint[0]+secondLinePoint[1]
    print("Second Slope is: " + str(a2))
    print(str(a1*b2-a2*b1))
    
    intersection = [
        -1*(b1*c2-b2*c1)/(a1*b2-a2*b1),
        -1*(a2*c1-a1*c2)/(a1*b2-a2*b1),
    ]
    return intersection

def findCircle(point1, point2, point3):
    #firstLineSlope = (point2[1] - point1[1])/(point2[0]-point1[0])*(-0.5)
    firstLinePoint = [(point2[0] + point1[0])/2, (point2[1]+point1[1])/2]
    
    #secondLineSlope = (point3[1] - point1[1])/(point3[0]-point1[0])*(-0.5)
    #secondLinePoint = [(point3[0] + point1[0])/2, (point3[1]+point1[1])/2]
    
    circleCenter = findIntersection(point1, point2, point1, point3)
    radius = abs(pythagMyBro(circleCenter, firstLinePoint))
    
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
    counter -= 2
    while counter > 2:
        point4 = [hull[counter-3], hull[counter-2]]
        point3 = [hull[counter-1], hull[counter]]
        point2 = [hull[newPoint-3], hull[newPoint-2]]
        point1 = [hull[newPoint-1], hull[newPoint]]
        print("\n")
        print(point1)
        print(point2)
        print(point3)
        print(point4)
        print("\n")
        firstLineSlope = (point2[1] - point1[1])/(point2[0]-point1[0])
        #print("firstLineSLope: " + str(firstLineSlope))
        
        secondLineSlope = (point4[1] - point3[1])/(point4[0]-point3[0])
       # print("secondLineSlope: " + str(secondLineSlope))
        intersection = findIntersection(point1, point2, point3, point4)
        print("\nIntersection Testing!   Points: " + str((counter/2)+0.5) + " " + str((counter/2)-0.5))
        print(str(point1[0]) + " " + str(point2[0]) + " " + str(intersection[0]) + " " + str(min([point1[0], point2[0], intersection[0]])))
        print(str(point1[1]) + " " + str(point2[1]) + " " + str(intersection[1]) + " " + str(min([point1[1], point2[1], intersection[1]])))
        print(str(point3[0]) + " " + str(point4[0]) + " " + str(intersection[0]) + " " + str(min([point3[0], point4[0], intersection[0]])))
        print(str(point3[1]) + " " + str(point4[1]) + " " + str(intersection[1]) + " " + str(min([point3[1], point4[1], intersection[1]])))
        print("\n")
        if min([point1[0], point2[0], intersection[0]]) != intersection[0] and max([point1[0], point2[0], intersection[0]]) != intersection[0] and min([point1[1], point2[1], intersection[1]]) != intersection[1] and max([point1[1], point2[1], intersection[1]]) != intersection[1] and min([point3[0], point4[0], intersection[0]]) != intersection[0] and max([point3[0], point4[0], intersection[0]]) != intersection[0] and min([point3[1], point4[1], intersection[1]]) != intersection[1] and max([point3[1], point4[1], intersection[1]]) != intersection[1]:
            return True
        
        counter -= 2
    return False

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
            #print(len(pointList))
            anything = myCanvas.create_line(pointList[0], pointList[1], hull[0], hull[1], fill="red")
            anything2 = myCanvas.create_polygon
            finishedHull = True
        else:
            if len(pointList) == 2:
                dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
            elif len(pointList) == 4 and len(hull) < 11:
                counter = len(hull)-1
                if counter > 5:
                    print("CheckForCross: " + str(checkForCross()))
                dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
                #print("We Did IT!")
                anything = myCanvas.create_line(pointList[0], pointList[1], pointList[2], pointList[3], fill="red")
                pointList.pop(0)
                pointList.pop(0)

        
myCanvas.pack()
myTk.bind("<Button-1>", draw_dots)
myTk.mainloop()

'''point1 = [0, 300]
point2 = [600, 320]

point3 = [200, 200]
point4 = [300, 400]

print(findIntersection(point1, point2, point3, point4))'''
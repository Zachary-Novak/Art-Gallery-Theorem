from asyncio import events
from tkinter import *
#import matplotlib.pyplot as plt
import math
import sys
import os
from turtle import left


class Polygon:
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    def draw_dots(self, event):
        if not self.finishedHull:
            x_coord = event.x
            y_coord = event.y
            self.pointList.append(x_coord)
            self.pointList.append(y_coord)
            self.hull.append(x_coord)
            self.hull.append(y_coord)
            #print(len(pointList))
            if len(self.destroyList) > 0:
                counter = len(self.destroyList)-1
                while counter >= 0:
                    self.myCanvas.delete(self.destroyList[counter])
                    counter -= 1
                self.destroyList.clear()
            if len(self.hull) > 4 and (math.sqrt(pow((y_coord-self.hull[1]), 2) + pow((x_coord-self.hull[0]), 2))) < 5:
                #print(len(pointList))
                #print("FoundEnd)")
                anything = self.myCanvas.create_line(self.pointList[0], self.pointList[1], self.hull[0], self.hull[1], fill="blue")
                self.hull.pop()
                self.hull.pop()
                self.finishedHull = True
            else:
                if len(self.pointList) == 2:
                    dot_circle = self.myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
                elif len(self.pointList) == 4 and not self.checkForCross():
                    counter = len(self.hull)-1
                    #if counter > 5:
                        #print("CheckForCross: " + str(checkForCross()))
                    dot_circle = self.myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)
                    #print("We Did IT!")
                    anything = self.myCanvas.create_line(self.pointList[0], self.pointList[1], self.pointList[2], self.pointList[3], fill="blue")
                    self.pointList.pop(0)
                    self.pointList.pop(0)
                else:
                    circleBreak = self.myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="red",width=0, tags="DestroyCircle")
                    lineBreak = self.myCanvas.create_line(self.pointList[0], self.pointList[1], self.pointList[2], self.pointList[3], fill="black", tags="DestroyLine")
                    self.destroyList.append(circleBreak)
                    self.destroyList.append(lineBreak)
                    self.hull.pop()
                    self.hull.pop()
                    self.pointList.pop()
                    self.pointList.pop()
        
    def __init__(self):
        self.myTk = Tk()
        self.myTk.title("Triangle Testing")

        self.myCanvas = Canvas(self.myTk, bd=4, bg="skyblue", cursor="circle", height=800, width=1200)
        self.pointList = []
        self.hull = []
        self.destroyList = []
        self.finishedHull = False
        
        self.myTk.bind("<Button-1>", self.draw_dots)

        quit_button = Button(self.myTk, text="Exit")
        quit_button.pack(side="bottom")
        quit_button["command"] = self.myTk.destroy
        triangulate_button = Button(self.myTk, text="Triangulate", highlightcolor="black")
        triangulate_button.pack(side="top")
        triangulate_button["command"] = self.triangulate
        draw_new_button = Button(self.myTk, text = "Clear")
        draw_new_button.pack(side="top")
        draw_new_button["command"] = self.myCanvas.delete("all")
        restart_button = Button(self.myTk, text="Restart")
        restart_button.pack(side="bottom")
        restart_button["command"] = self.restart_program
        
    def pythagMyBro(self, point1, point2):
        return math.sqrt(pow(point2[1] - point1[1], 2) + pow(point2[0] - point1[0]))

    def insideCircle(self, circle, point):
        center = circle[0]
        distance = circle[1]
        if self.pythagMyBro(center, point) < distance:
            return True
        else:
            return False

    def findIntersection(self, point1, point2, point3, point4):
            
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

    def findCircle(self, point1, point2, point3):
        circleCenter = self.findIntersection(point1, point2, point2, point3)
        radius = abs(self.pythagMyBro(circleCenter, point1))
        
        return [circleCenter, radius]
        
    def leftOf(self, a, b, c):
        area = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
        if area > 0:
            return False
        else:
            return True

    def checkForCross(self):
        counter = len(self.hull)-1
        #print("counter is " + str(counter))
        #print("hull is ")
        #print(self.hull)
        #print("\n")
        newPoint = counter
        counter -= 4
        while counter > 2:
            point4 = [self.hull[counter-3], self.hull[counter-2]]
            point3 = [self.hull[counter-1], self.hull[counter]]
            point2 = [self.hull[newPoint-3], self.hull[newPoint-2]]
            point1 = [self.hull[newPoint-1], self.hull[newPoint]]
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
            intersection = self.findIntersection(point1, point2, point3, point4)
            #print("\nIntersection Testing!   Points: " + str((counter/2)+0.5) + " " + str((counter/2)-0.5))
            #print(str(point1[0]) + " " + str(point2[0]) + " " + str(intersection[0]) + " " + str(min([point1[0], point2[0], intersection[0]])))
            #print(str(point1[1]) + " " + str(point2[1]) + " " + str(intersection[1]) + " " + str(min([point1[1], point2[1], intersection[1]])))
            #print(str(point3[0]) + " " + str(point4[0]) + " " + str(intersection[0]) + " " + str(min([point3[0], point4[0], intersection[0]])))
            #print(str(point3[1]) + " " + str(point4[1]) + " " + str(intersection[1]) + " " + str(min([point3[1], point4[1], intersection[1]])))
            #print("\n")
            if (intersection != [float('inf'), float('inf')]):
                #print("First Passed")
                if (min([point1[0], point2[0], intersection[0]]) != intersection[0] and max([point1[0], point2[0], intersection[0]]) != intersection[0]) or (intersection[0] == point1[0] and intersection[0] == point2[0]):# and (intersection[1] != point1[1] and intersection[1] != point2[1])):
                    #print("Second Passed")
                    if (min([point1[1], point2[1], intersection[1]]) != intersection[1] and max([point1[1], point2[1], intersection[1]]) != intersection[1]) or (intersection[1] == point1[1] and intersection[1] == point2[1]):# and (intersection[0] != point1[0] and intersection[0] != point2[0])):
                        #print("Third Passed")
                        if (min([point3[0], point4[0], intersection[0]]) != intersection[0] and max([point3[0], point4[0], intersection[0]]) != intersection[0]) or (intersection[0] == point3[0] and intersection[0] == point4[0]):# and (intersection[1] != point3[1] and intersection[1] != point4[1])):
                            #print("Fourth Passed")
                            if (min([point3[1], point4[1], intersection[1]]) != intersection[1] and max([point3[1], point4[1], intersection[1]]) != intersection[1])  or (intersection[1] == point3[1] and intersection[1] == point4[1]):# and (intersection[0] != point3[0] and intersection[0] != point4[0])):
                                #print("\nIntersection Testing!   Points: " + str((counter/2)+0.5) + " " + str((counter/2)-0.5))
                                #print(point1)
                                #print(point2)
                                #print(point3)
                                #print(point4)
                                #print(intersection)
                                return True
            '''if (intersection != [float('inf'), float('inf')] and 
                ((intersection[1] == point1[1] or intersection[1] == point2[1]) and 
                    (min([point1[0], point2[0], intersection[0]]) != intersection[0] and max([point1[0], point2[0], intersection[0]]) != intersection[0])) or
                ((intersection[0] == point1[0] or intersection[0] == point2[0]))
            )'''

            counter -= 2
        return False
    
    
    
    def findAngle(self, point1, point2, point3):
        return math.degrees(math.atan2(point3[1] - point2[1], point3[0] - point2[0]) - math.atan2(point1[1]-point2[1],point1[0] - point2[0]))
    
    def findSlopeFromTwoPoints(self, point1, point2):
        slope = (point2[1] - point1[1])/(point2[0] - point1[0])
        return slope
    
    def findSlopeFromThreePoints(self, point1, point2, point3):
        slope1 = (point2[1]-point1[1])/(point2[0]-point1[0])
        #print(slope1)
        slope2 = (point3[1]-point2[1])/(point3[0]-point2[0])
        #print(slope2)
        finalSlope = (slope1+slope2)/2
        #print(finalSlope)
        return finalSlope
    
    def triangulate(self):
        
        hullCopy = self.hull
        
        point1 = [self.hull[0], self.hull[1]]
        point2 = [self.hull[2], self.hull[3]]
        point3 = [self.hull[4], self.hull[5]]
        print(point1)
        print(point2)
        print(point3)
        
        #castingSlope = self.findSlopeFromThreePoints(point1, point2, point3)
        
        #dot_circle = self.myCanvas.create_oval(point2[0]-5,point2[1]-5,point2[0]+5,point2[1]+5,outline="black",fill="black",width=0)
        
        '''x = 200 + point2[0]
        y = 200 * castingSlope + point2[1]'''
        
        x = (point3[0] + point1[0])/2
        y = (point3[1] + point1[1])/2
        endPoint = [x, y]
        
        
        endSlope = self.findSlopeFromTwoPoints(point2, endPoint)
        if endPoint[0] > point2[0]:
            endPoint[0] = endPoint[0] + 1000
            endPoint[1] = endPoint[1] + (endSlope*1000)
        else:
            endPoint[0] = endPoint[0] - 1000
            endPoint[1] = endPoint[1] - (endSlope*1000)
        
        iterator = []
        isEar = False
        iterator.clear()
        counter = 2
        while counter < len(self.hull):
            iterator.append(counter)
            counter += 1
        counter = 0
        while counter < 4:
            iterator.append(counter)
            counter += 1
            
        print(iterator)
        
        #intersection = self.findIntersection(point2, endPoint, point1, point3)
        dot_circle = self.myCanvas.create_oval(point1[0]-5,point1[1]-5,point1[0]+5,point1[1]+5,outline="black",fill="black",width=0)
        
        dot_circle = self.myCanvas.create_line([point2[0], point2[1]], endPoint, fill="black")
        
        dot_circle = self.myCanvas.create_oval(point3[0]-5,point3[1]-5,point3[0]+5,point3[1]+5,outline="black",fill="black",width=0)
        #dot_circle = self.myCanvas.create_oval(intersection[0]-5,intersection[1]-5,intersection[0]+5,intersection[1]+5,outline="red",fill="red",width=0)
        totalIntersections = 0
        i = 0
        while i < (len(iterator)-4):
            point1 = [hullCopy[iterator[i]], hullCopy[iterator[i+1]]]
            point3 = [hullCopy[iterator[i+2]], hullCopy[iterator[i+3]]]
            intersection = self.findIntersection(point2, endPoint, point1, point3)
            if (intersection != [float('inf'), float('inf')]) and intersection != point2:
                print("First Passed")
                if (min([point1[0], point3[0], intersection[0]]) != intersection[0] and max([point1[0], point3[0], intersection[0]]) != intersection[0]) or (intersection[0] == point1[0] and intersection[0] == point3[0]):
                    print("Second Passed")
                    if (min([point1[1], point3[1], intersection[1]]) != intersection[1] and max([point1[1], point3[1], intersection[1]]) != intersection[1]) or (intersection[1] == point3[1] and intersection[1] == point3[1]):
                        print("Third Passed")
                        if (min([endPoint[1], point2[1], intersection[1]]) != intersection[1] and max([endPoint[1], point2[1], intersection[1]]) != intersection[1]) or (intersection[1] == endPoint[1] and intersection[1] == point2[1]):
                            totalIntersections += 1
                            dot_circle = self.myCanvas.create_oval(intersection[0]-5,intersection[1]-5,intersection[0]+5,intersection[1]+5,outline="yellow",fill="yellow",width=0)
            i = i + 2
        print("Total Intersctions: " + str(totalIntersections))             
        
        

        
        #x = math.sqrt(pow(100, 2)/(pow(castingSlope, 2) + 1)) + point2[0]
        #y = x*castingSlope + point2[1]
        
        '''angle1 = self.findAngle(endPoint, point2, [point2[0] + 1, point2[1]])
        angle2 = self.findAngle(point1, point2, [point2[0] + 1, point2[1]])
        if (angle2 < 0):
            angle2 = angle2 + 360
        angle3 = self.findAngle(point3, point2, [point2[0] + 1, point2[1]])
        if (angle3 < 0):
            angle3 = angle3 + 360'''
            
        '''firstCheck = self.leftOf(point2, endPoint, point1)
        print(firstCheck)
        secondCheck = self.leftOf(point2, endPoint, point3)
        print(secondCheck)
        
        selfCheck1 = self.leftOf(point2, point1, endPoint)
        print(selfCheck1)
        selfCheck2 = self.leftOf(point2, point3, endPoint)
        print(selfCheck2)
        if firstCheck != secondCheck and not firstCheck == selfCheck2 and not secondCheck == selfCheck1:
            print("Success")'''
        
        '''angle1 = self.findAngle(endPoint, point2, point1)
        angle2 = self.findAngle(point1, point2, point3)
        
        angles = [angle1, angle2]'''
        
        
        #print(angles)
        
        '''iterator = [point2, point3, point1]
        j = 1
        print("Doing this")
        print(endPoint)
        intersection = self.findIntersection(point2, endPoint, point1, point3)'''

        
        
        '''i = 0
        iterator = []
        while i < len(self.hull)-6:
            isEar = False
            iterator.clear()
            counter = i
            while counter < len(self.hull):
                iterator.append(counter)
                counter += 1
            counter = 0
            while counter < i:
                iterator.append(counter)
                counter += 1
            
            castingSlope = self.findSlopeFromThreePoints([self.hull[iterator[i]], self.hull[iterator[i+1]]], [self.hull[iterator[i+2]], self.hull[iterator[i+3]]], [self.hull[iterator[i+4]], self.hull[iterator[i+5]]])

            x = math.sqrt(pow(2000, 2)/(pow(castingSlope, 2) + 1)) + self.hull[i]
            y = x*castingSlope + self.hull[i+1]
            
            
            endPoint = [x, y]
            totalIntersections = 0
            j = 0
            while j < len(iterator)-6:
                #print(type([self.hull[iterator[i]], self.hull[iterator[i+1]]]))
                #print(type(endPoint))
                #print(type([self.hull[iterator[j+2]], self.hull[iterator[j+3]]]))
                #print(type([self.hull[iterator[j+4]], self.hull[iterator[j+5]]]))
                #intersectionParameter = [[self.hull[iterator[i]], self.hull[iterator[i+1]]], endPoint, [self.hull[iterator[j+2]], self.hull[iterator[j+3]]], [self.hull[iterator[j+4]], self.hull[iterator[j+5]]]]
                #print(intersectionParameter)
                dot_circle = self.myCanvas.create_line([self.hull[iterator[i]], self.hull[iterator[i+1]]], endPoint, fill="Black")
                print("Doing this")
                print(endPoint)
                intersection = self.findIntersection([self.hull[iterator[i]], self.hull[iterator[i+1]]], endPoint, [self.hull[iterator[j+2]], self.hull[iterator[j+3]]], [self.hull[iterator[j+4]], self.hull[iterator[j+5]]])
                if intersection == True:
                    totalIntersections += 1
                j += 2
            if totalIntersections%2 == 0:
                print("Didn't Find Ear, " + str(totalIntersections) + " intersections")
                isEar = False
            else:
                isEar = True
                print("Found Ear, " + str(totalIntersections) + " intersections")
                
            if isEar:
                print("adding Triangle")
                triangle = self.myCanvas.create_polygon(self.hull[iterator[i]], self.hull[iterator[i+1]], self.hull[iterator[j+2]], self.hull[iterator[j+3]], self.hull[iterator[j+4], self.hull[iterator[j+5]]], fill="lemonchiffon")
            print(i)
            
            i += 2'''
    
    def removeCollinearPoints(self, point1, point2, point3):
        if self.leftOf(point1, point2, point3) == 0:
            self.hull.remove(point2)
                    
    def createScreen(self):
        self.myCanvas.pack()
        self.myTk.mainloop()

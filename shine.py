from tkinter import *
import math

myTk = Tk()
myTk.title("Clicking and spacebar do things")
myCanvas = Canvas(myTk, bd=4, bg="skyblue", cursor="circle", height = 600, width = 1000)

'''variables that the light takes as input'''
light = [] #coordinates of the light source
pointList = []#list of points stored as [xcoord1, ycoord1], [xcoord2, ycoord2], ...
pointdraw = []#variable keeping track of each line drawn
pointmap = dict() #map that takes in a value equal to (pointindex1)*(pointindex-1)/2+pointinex2 and outputs the index of the edge (point1, point2)
edgeList = [] #variable list stored as a trio of numbers where the first two are the indices of the points and the third is the type of segment. [0,1, 0] indicates an solid wall made by the first two points in the list.
edgedraw = [] #variable for keeping track of each edge drawn
edgemap = dict() #hash map that takes in the index of an edge and outputs the indices of the (maximum of 2) triangles connected to the edge
linetype = 0 #keeps track of the type of the line being added
triList = [] #list of the 3 indices of the points which make up the triangle
edgeQueue = [] #list of edges which we need to do math for
triangleinit = 0 #index of triangle containing the light source
'''variables for my triangulation plotting'''
pc = -1 #number of polygonpoints plotted.
trianglemaker = [] #for adding a triangle in the drawsegment section
pointtracker = 0 #which point we are at in adding a new triangle
pointsave = []
edgetypesave = [0,0,0]
shineQ = False
absorbedQ = False
lightList = [] #variable that keeps track of every shape of light drawn

def d2(point1, point2): #distance, but without the square root
    return pow((point2[1]-point1[1]),2)+pow(point2[0]-point1[0],2)
def draw_segment(event): #used to generate the triangulated polygon, don't use in actual program except as a reference to how data is stored
    global pc, light, pointList, pointdraw, pointmap, edgeList, edgedraw, edgemap, linetype, pointtracker, trianglemaker, pointsave
    if pc==-1:
        light = [event.x, event.y]
        lightnode = myCanvas.create_oval(light[0]-5,light[1]-5,light[0]+5,light[1]+5,fill="yellow",width=0)
        pc += 1
    elif pc < 3:
        pointList.append([event.x, event.y])
        pointdraw.append(myCanvas.create_oval(pointList[pc][0]-5,pointList[pc][1]-5,pointList[pc][0]+5,pointList[pc][1]+5,fill="green",width=0))
        edgetypesave[pc] = linetype
        if pc == 2:
            edgeList = [[1,0, edgetypesave[0]], [2,1, edgetypesave[1]], [2,0, edgetypesave[2]]]
            edgedraw.append(myCanvas.create_line(pointList[edgeList[0][0]][0], pointList[edgeList[0][0]][1], pointList[edgeList[0][1]][0], pointList[edgeList[0][1]][1], fill=["black", "magenta"][edgetypesave[0]]))
            edgedraw.append(myCanvas.create_line(pointList[edgeList[1][0]][0], pointList[edgeList[1][0]][1], pointList[edgeList[1][1]][0], pointList[edgeList[1][1]][1], fill=["black", "magenta"][edgetypesave[1]]))
            edgedraw.append(myCanvas.create_line(pointList[edgeList[2][0]][0], pointList[edgeList[2][0]][1], pointList[edgeList[2][1]][0], pointList[edgeList[2][1]][1], fill=["black", "magenta"][edgetypesave[2]]))
            pointmap[0] = 0
            pointmap[2] = 1
            pointmap[1] = 2
            edgemap[0] = [0]
            edgemap[1] = [0]
            edgemap[2] = [0]
            triList.append([0,1,2])
        pc += 1
    else:
        if pointtracker!=1:
            distindex = 0
            dist = d2([event.x, event.y], [pointList[0][0], pointList[0][1]])
            for i in range(len(pointList)):
                temp = d2([event.x, event.y], [pointList[i][0], pointList[i][1]])
                if temp < dist:
                    distindex = i
                    dist = temp
            trianglemaker.append(myCanvas.create_oval(pointList[distindex][0]-5,pointList[distindex][1]-5,pointList[distindex][0]+5,pointList[distindex][1]+5,outline="black",fill="red",width=0))
            pointsave.append(distindex)
        else:
            pointsave.append([event.x, event.y])
            trianglemaker.append(myCanvas.create_oval(event.x-5,event.y-5,event.x+5,event.y+5,fill="green",width=0))
            edgetypesave[0] = linetype
        if pointtracker == 2:
            edgetypesave[1] = linetype
            if pointsave[0] < pointsave[2]:
                temp = pointsave[0]
                pointsave[0] = pointsave[2]
                pointsave[2] = temp
                edgetypesave[0]+=edgetypesave[1]
                edgetypesave[1] = edgetypesave[0]-edgetypesave[1]
                edgetypesave[0] -= edgetypesave[1]
            if pointsave[0]==pointsave[2] or (pointsave[0]*(pointsave[0]-1)/2+pointsave[2]) not in pointmap.keys():
                for i in range(3):
                    myCanvas.delete(trianglemaker[i])
            else:
                pointList.append(pointsave[1])
                myCanvas.delete(trianglemaker[0], trianglemaker[2])
                pointdraw = trianglemaker[1]
                pointmap[pc*(pc-1)/2+pointsave[2]] = len(edgeList)
                edgeList.append([pc, pointsave[2], linetype])
                edgedraw.append(myCanvas.create_line(pointList[edgeList[len(edgeList)-1][0]][0], pointList[edgeList[len(edgeList)-1][0]][1], pointList[edgeList[len(edgeList)-1][1]][0], pointList[edgeList[len(edgeList)-1][1]][1], fill=["black", "magenta"][edgetypesave[1]]))
                pointmap[pc*(pc-1)/2+pointsave[0]] = len(edgeList)
                edgeList.append([pc, pointsave[0], linetype])
                edgedraw.append(myCanvas.create_line(pointList[edgeList[len(edgeList)-1][0]][0], pointList[edgeList[len(edgeList)-1][0]][1], pointList[edgeList[len(edgeList)-1][1]][0], pointList[edgeList[len(edgeList)-1][1]][1], fill=["black", "magenta"][edgetypesave[0]]))
                myCanvas.itemconfig(edgedraw[pointmap[pointsave[0]*(pointsave[0]-1)/2+pointsave[2]]], fill="cyan")
                edgeList[pointmap[pointsave[0]*(pointsave[0]-1)/2+pointsave[2]]][2] = 2
                edgemap[pc*(pc-1)/2+pointsave[2]] = [len(triList)]
                edgemap[pc*(pc-1)/2+pointsave[0]] = [len(triList)]
                edgemap[pointsave[0]*(pointsave[0]-1)/2+pointsave[2]].append(len(triList))
                triList.append([pointList[2], pointList[0], pc])
                pc += 1
            pointsave = []
            trianglemaker = []
        pointtracker = (pointtracker+1)%3

def change_line_type(event):
    global linetype, absorbedQ
    if not shineQ:
        linetype = 1-linetype
    elif not absorbedQ:
        if len(edgeQueue)==0:
            for i in range(3):
                reflect = [light[0], light[1]]
                if(edgeList[pointmap[triList[triangleinit][math.ceil(i/2)+1]*(triList[triangleinit][math.ceil(i/2)+1]-1)/2+triList[triangleinit][math.floor(i/2)]]][2] > 0):
                    temp = edgemap[pointmap[triList[triangleinit][math.ceil(i/2)+1]*(triList[triangleinit][math.ceil(i/2)+1]-1)/2+triList[triangleinit][math.floor(i/2)]]]
                    nexttri = triangleinit
                    if(edgeList[pointmap[triList[triangleinit][math.ceil(i/2)+1]*(triList[triangleinit][math.ceil(i/2)+1]-1)/2+triList[triangleinit][math.floor(i/2)]]][2] == 2):
                        print(nexttri)
                        nexttri = temp[0]+temp[1]-triangleinit
                    if edgeList[pointmap[triList[triangleinit][math.ceil(i/2)+1]*(triList[triangleinit][math.ceil(i/2)+1]-1)/2+triList[triangleinit][math.floor(i/2)]]][2] == 1:
                        v1 = [light[0]-pointList[triList[triangleinit][math.ceil(i/2)+1]][0], light[1]-pointList[triList[triangleinit][math.ceil(i/2)+1]][1]]
                        v2 = [pointList[triList[triangleinit][math.floor(i/2)]][0]-pointList[triList[triangleinit][math.ceil(i/2)+1]][0], pointList[triList[triangleinit][math.floor(i/2)]][1]-pointList[triList[triangleinit][math.ceil(i/2)+1]][1]]
                        cosnum = v1[0]*v2[0]+v1[1]*v2[1]
                        sinnum = v1[0]*v2[1]-v1[1]*v2[0]
                        prodnormsq = (v1[0]*v1[0]+v1[1]*v1[1])*(v2[0]*v2[0]+v2[1]*v2[1])
                        rx = ((cosnum*cosnum-sinnum*sinnum)*v1[0]-2*cosnum*sinnum*v1[1])/prodnormsq+pointList[triList[triangleinit][math.ceil(i/2)+1]][0]
                        ry = (2*cosnum*sinnum*v1[0]+(cosnum*cosnum-sinnum*sinnum)*v1[1])/prodnormsq+pointList[triList[triangleinit][math.ceil(i/2)+1]][1]
                        reflect = [rx, ry]
                        nexttri = triangleinit
                    #edgeQueue.append([source, intersect1, intersect2, edgeindex, triangleindex])
                    edgeQueue.append([[reflect[0], reflect[1]], pointList[triList[triangleinit][math.ceil(i/2)+1]], pointList[triList[triangleinit][math.floor(i/2)]], pointmap[triList[triangleinit][math.ceil(i/2)+1]*(triList[triangleinit][math.ceil(i/2)+1]-1)/2+triList[triangleinit][math.floor(i/2)]], nexttri])
                    print(edgeQueue)
                lightList.append(myCanvas.create_polygon(reflect[0], reflect[1], pointList[triList[triangleinit][math.ceil(i/2+1)]][0], pointList[triList[triangleinit][math.ceil(i/2+1)]][1], pointList[triList[triangleinit][math.floor(i/2)]][0], pointList[triList[triangleinit][math.floor(i/2)]][1], fill = "yellow"))
        if len(edgeQueue)==0:
            absorbedQ = 1
    '''if linetype == 0:
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
        myCanvas.create_polygon(rx, ry, pointList[0], pointList[1], pointList[2], pointList[3], fill="green")'''
def initShine(event):
    global shineQ
    shineQ = 1 
        
myCanvas.pack()
myTk.bind("<Button-1>", draw_segment)
myTk.bind("<space>", change_line_type)
myTk.bind("<Return>", initShine)
myTk.mainloop()

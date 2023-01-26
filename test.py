from tkinter import *

myTk = Tk()
myTk.title("Triangle Testing")

myCanvas = Canvas(myTk, bd=5, bg="ivory", cursor="circle", height=300, width=300)
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

def InTriangle(a, b, c, p):
	L = [0, 0, 0]
	eps = 0.0000001
	# calculate barycentric coefficients for point p
	# eps is needed as error correction since for very small distances denom->0
	L[0] = ((b[1] - c[1]) * (p[0] - c[0]) + (c[0] - b[0]) * (p[1] - c[1])) \
		  /(((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])) + eps)
	L[1] = ((c[1] - a[1]) * (p[0] - c[0]) + (a[0] - c[0]) * (p[1] - c[1])) \
		  /(((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1])) + eps)
	L[2] = 1 - L[0] - L[1]
	# check if p lies in triangle (a, b, c)
	for x in L:
		if x > 1 or x < 0:
			return False  
	return True  

def IsConvex(a, b, c):
	cross_product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
	if cross_product >= 0:
		return True 
	return False 


myCanvas.pack()
myTk.bind("<Button-1>", draw_dots)
myTk.mainloop()

import tkinter as tk
import math

window = tk.Tk()
window.title("Archery Score Tracker")

myCanvas = tk.Canvas(window, width=400, height=600)
myCanvas.pack()

r = 180

c1 = myCanvas.create_oval(200-r,300-r,200+r,300+r,outline="black",fill="white")
c2 = myCanvas.create_oval(200-(4/5)*r,300-(4/5)*r,200+(4/5)*r,300+(4/5)*r,outline="black",fill="black")
c3 = myCanvas.create_oval(200-(3/5)*r,300-(3/5)*r,200+(3/5)*r,300+(3/5)*r,outline="black",fill="blue")
c4 = myCanvas.create_oval(200-(2/5)*r,300-(2/5)*r,200+(2/5)*r,300+(2/5)*r,outline="black",fill="red")
c5 = myCanvas.create_oval(200-(1/5)*r,300-(1/5)*r,200+(1/5)*r,300+(1/5)*r,outline="black",fill="yellow")

display_label = tk.Label(window, text="Scores:")
display_label.place(x=0, y=580)


totalscore = 0
total_display = tk.Label(window, text="Total:" + str(totalscore))
total_display.pack(side="left")      

def draw_dots(event):
    
    x_coord = event.x
    y_coord = event.y
    dot_circle = myCanvas.create_oval(x_coord-5,y_coord-5,x_coord+5,y_coord+5,outline="black",fill="green",width=0)

    global score
    global totalscore
    hypot = math.sqrt((x_coord-200)**2+(y_coord-300)**2)


    if hypot < (1/5)*r:
        score = 5
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        total_display.place(x=200,y=590,anchor="center")
        #total_display.pack(side="bottom")

    elif hypot < (2/5)*r:
        score = 4
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        total_display.place(x=200,y=590,anchor="center")



    elif hypot < (3/5)*r:
        score = 3
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        #total_display.pack(side="bottom")
        total_display.place(x=200,y=590,anchor="center")

    elif hypot < (4/5)*r:
        score = 2
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        #total_display.pack(side="bottom")
        total_display.place(x=200,y=590,anchor="center")

    elif hypot < r:
        score = 1
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        #total_display.pack(side="bottom")
        total_display.place(x=200,y=590,anchor="center")



    else:
        score = 0
        score_display = tk.Label(window, text=str(score))
        score_display.pack(side="left")
        totalscore+=score
        total_display["text"]="Total:" + str(totalscore)
        #total_display.pack(side="bottom")
        total_display.place(x=200,y=590,anchor="center")

        
window.bind("<Button-1>", draw_dots)        


quitButton = tk.Button(window, text="Quit")
quitButton.pack(side="bottom")
quitButton["command"] = window.destroy
quitButton.pack(side="bottom")




window.mainloop()        
                                 


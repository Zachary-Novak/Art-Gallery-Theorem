import PlottingTriangle
import Polygon
from tkinter import *

class Guard:
    def draw_polygon(self, event):
        # check whether the guard placed is inside the polygon or not
        x_coord = event.x
        y_coord = event.y
        
        
import math
import time

from field import Field
from Tkinter import *

class RushVisualisation:
    def __init__(self, length, vehicles, field):
        width = length
        height = length
        self.width = width
        self.height = height
        self.max_dim = max(width + 0.5, height)
        self.field = field

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(width, height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw gray squares for tiles
        self.tiles = {}
        for i in range(width):
            for j in range(height):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                             fill = "gray")

        # Draw gridlines
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)
        for vehicle in vehicles:
            self.car(vehicle, field, length)

        endx1, endy1 = self._map_coords(6, 2)
        endx2, endy2 = self._map_coords(6.3, 3)
        self.w.create_rectangle(endx1, endy1, endx2, endy2, fill = "gray")

        self.master.update()

        self.master.mainloop()


    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((y - self.height / 2.0) / self.max_dim))

    def car(self, vehicle, field, length):
        x1, y1 = vehicle.getCoor(field)[0]
        x2, y2 = vehicle.getCoor(field)[1]
        # x1, y1, x2, y2 = vehicle.getCoor(field)
        xa1, ya1 = self._map_coords(x1 - 1,y1 - 1)
        xa2, ya2 = self._map_coords(x2, y2)
        return self.w.create_rectangle(xa1, ya1, xa2, ya2, fill=vehicle.getColor())

    

class Vehicle(object):
    def __init__(self, name, orientation, color):
        self.name = name
        self.orientation = orientation
        self.color = color

    def getColor(self):
        return self.color

    def getCoor(self, field):
        self.len_tiles = len(field.tiles)
        rowx = {}
        xcoor = []
        coordinates = []
        for i in range(field.length):
            rowx[i+1] = field.tiles[(len(field.tiles)/field.length)*(i):(len(field.tiles)/field.length)*(i+1)]
            if self.name in rowx[i+1]:
                xcoor.append(i+1)

        for row in rowx.values():
            for i in range(field.length):
                if row[i] == self.name:
                    for coor in xcoor:
                        if (i+1,coor) not in coordinates:
                            coordinates.append((i+1,coor))
        print coordinates
        if len(coordinates) > 1:

            miniy = coordinates[0][1]
            maxiy = coordinates[1][1]
            minix = coordinates[0][0]
            maxix = coordinates[1][0]
            if len(coordinates) == 3:

                for coor in coordinates:
                    if self.orientation == "vertical":
                        if miniy > coor[1]:
                            miniy = coor[1]
                        if maxiy < coor[1]:
                            maxiy = coor[1]
                    else:
                        if minix > coor[0]:
                            minix = coor[0]
                        if maxix < coor[0]:
                            maxix = coor[0]

            return (minix,miniy),(maxix,maxiy)
        return (0,0),(0,0)

def vehicles1():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "green"),
        "C": Vehicle("C", "horizontal", "blue"),
        "D": Vehicle("D", "vertical", "cyan"),
        "E": Vehicle("E", "vertical", "orange"),
        "F": Vehicle("F", "horizontal", "green"),
        "G": Vehicle("G", "vertical", "cyan"),
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "horizontal", "green"),
        "J": Vehicle("J", "vertical", "yellow"),
        "K": Vehicle("K", "horizontal", "blue"),
        "L": Vehicle("L", "vertical", "orange"),
        "R": Vehicle("R", "horizontal", "red")
    }
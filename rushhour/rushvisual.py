import math
import time

from field import Field
from Tkinter import *

class RushVisualisation:
    def __init__(self, length, vehicles, fields, delay = 0.2):
        width = length
        height = length
        self.width = width
        self.height = height
        self.max_dim = max(width + 0.5, height)
        self.fields = fields
        self.delay = delay

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
        draw = []
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)

        for field in fields:
            self.removeCar(draw)
            for vehicle in vehicles:
                # self.car(vehicle, field, length)
                draw.append(self.car(vehicle, field, length))
            self.master.update()
            time.sleep(self.delay)

        # for vehicle in vehicles:
        #     print len(vehicles)
        #     print vehicle.getName()
        #     self.car(vehicle, field, length)

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
        x1, y1 = vehicle.getCoor(field, length)[0]
        # print x1, y1
        x2, y2 = vehicle.getCoor(field, length)[1]
        # print x2, y2
        xa1, ya1 = self._map_coords(x1 - 1,y1 - 1)
        xa2, ya2 = self._map_coords(x2, y2)
        return self.w.create_rectangle(xa1, ya1, xa2, ya2, fill=vehicle.getColor())

    def removeCar(self, allCars):
        # remove all the cars
        if allCars:
            for car in allCars:
                self.w.delete(car)
                self.master.update_idletasks()

    

class Vehicle(object):
    def __init__(self, name, orientation, color):
        self.name = name
        self.orientation = orientation
        self.color = color

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

    def getCoor(self, field, length):
        self.len_tiles = len(field)
        rowx = {}
        xcoor = []
        coordinates = []
        for i in range(length):
            rowx[i+1] = field[self.len_tiles/length*(i):self.len_tiles/length*(i+1)]
            if self.name in rowx[i+1]:
                xcoor.append(i+1)

        for row in rowx.values():
            for i in range(length):
                if row[i] == self.name:
                    for coor in xcoor:
                        if (i+1,coor) not in coordinates:
                            coordinates.append((i+1,coor))
        
        minix = coordinates[0][0]
        miniy = coordinates[0][1]

        if len(coordinates) == 2:
            maxix = coordinates[1][0]
            maxiy = coordinates[1][1]

        else:
            maxix = coordinates[2][0]
            maxiy = coordinates[2][1]

        return (minix,miniy),(maxix,maxiy)

def vehicles1():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "blue"),
        "C": Vehicle("C", "vertical", "purple"),
        "D": Vehicle("D", "vertical", "orange"),
        "E": Vehicle("E", "horizontal", "green"),
        "F": Vehicle("F", "horizontal", "orange"),
        "G": Vehicle("G", "horizontal", "blue"),
        "H": Vehicle("H", "vertical", "yellow"),
        "R": Vehicle("R", "horizontal", "red")
    }


import math
import time
import copy

from field import Field
from Tkinter import *

class RushVisualisation:
    def __init__(self, length, vehicles, fields):
        self.length = length
        self.width = self.length
        self.height = self.length
        self.max_dim = max(self.width + 0.5, self.height)
        self.vehicles = vehicles
        self.fields = fields


        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # self.vis(self.fields, vehicles)

        b = Button(self.master, text="Visualisatie", command=lambda: self.vis(self.fields, self.vehicles, self.width, self.height))
        b.pack()
        self.master.mainloop()


    def vis(self, fields, width, height, vehicles, delay = 0.2):
        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(self.width, self.height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw gray squares for tiles
        self.tiles = {}
        for i in range(self.width):
            for j in range(self.height):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                             fill = "gray")

        # Draw gridlines
        for i in range(self.width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, self.height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(self.height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(self.width, i)
            self.w.create_line(x1, y1, x2, y2)

        endx1, endy1 = self._map_coords(6, 2)
        endx2, endy2 = self._map_coords(6.3, 3)
        self.w.create_rectangle(endx1, endy1, endx2, endy2, fill = "gray")
        # print "Visualisatie"
        draw = []
        for vehicle in self.vehicles:
                # self.car(vehicle, field, length)
                draw.append(self.car(vehicle, fields[0], self.length))
        for field in range(len(fields)):
            if field > 0:
                for num in range(len(fields[field])):
                    # print fields[field][num], fields[field - 1][num]
                    if fields[field][num] != fields[field - 1][num]:
                        for element in draw:
                            print element[1].getName(), fields[field][num]
                            if element[1].getName() == fields[field][num]:
                                the_car = copy.copy(element[1])
                                self.removeCar(element)
                                draw.remove(element)
                                draw.append(self.car(the_car, fields[field], self.length))
            # for vehicle in self.vehicles:
            #     # self.car(vehicle, field, length)
            #     draw.append(self.car(vehicle, fields[field], self.length))
            self.master.update()
            time.sleep(delay)        


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
        return self.w.create_rectangle(xa1, ya1, xa2, ya2, fill=vehicle.getColor()), vehicle

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


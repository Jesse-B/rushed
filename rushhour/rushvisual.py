import math
import time
import copy

from field import Field
from Tkinter import *

class RushVisualisation:
    def __init__(self, length, vehicles, begin_field, canvas, the_object):
        self.length = length
        self.width = self.length
        self.height = self.length
        self.max_dim = max(self.width + 0.5, self.height)
        self.vehicles = vehicles
        self.fields = begin_field
        self.w = canvas
        self.master = the_object
        self.w.delete("all")
        self.thebegin = self.begin()
        
        # button5.pack()

        
    def begin(self):
        self.text = Label(self.master, text="Beginveld")
        self.text.pack()
        self.text.place(x=225, y=465)
        

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
            draw.append(self.car(vehicle, self.fields, self.length))
        return (draw, self.text)

        

    def run(self, fields, button, delay = 0.2):
        steps = 0
        self.game = self.begin()
        draw = self.game[0]
        text = self.game[1]

        for field in range(len(fields)):
            steps += 1
            text.destroy()
            text = Label(self.master, text=("Aantal stappen: " + str(steps)))
            text.pack()
            text.place(x=210, y=465)

            if field > 0:
                for num in range(len(fields[field])):
                    # print fields[field][num], fields[field - 1][num]
                    if fields[field][num] != fields[field - 1][num]:
                        for element in draw:
                            if element[1].getName() == fields[field][num]:
                                the_car = copy.copy(element[1])
                                self.removeCar(element)
                                draw.remove(element)
                                draw.append(self.car(the_car, fields[field], self.length))

            self.master.update()
            time.sleep(delay)  
            button.pack_forget()      


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

def vehicles2():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "green"),
        "C": Vehicle("C", "horizontal", "blue"),
        "D": Vehicle("D", "vertical", "cyan"),
        "E": Vehicle("E", "horizontal", "orange"),
        "F": Vehicle("F", "horizontal", "green"),
        "G": Vehicle("G", "vertical", "cyan"),
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "horizontal", "green"),
        "J": Vehicle("J", "vertical", "yellow"),
        "K": Vehicle("K", "horizontal", "blue"),
        "L": Vehicle("L", "horizontal", "orange"),
        "R": Vehicle("R", "horizontal", "red")
        }

def vehicles3():
    return {
        "A": Vehicle("A", "horizontal", "blue"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "horizontal", "orange"),
        "D": Vehicle("D", "vertical", "blue"), 
        "E": Vehicle("E", "horizontal", "green"),
        "F": Vehicle("F", "vertical", "cyan"), 
        "G": Vehicle("G", "horizontal", "green"), 
        "H": Vehicle("H", "horizontal", "blue"),
        "I": Vehicle("I", "vertical", "cyan"), 
        "J": Vehicle("J", "vertical", "orange"),
        "K": Vehicle("K", "vertical", "green"),
        "L": Vehicle("L", "horizontal", "green"),
        "R": Vehicle("R", "horizontal", "red")
    }

def vehicles4():
    return {
        "A": Vehicle("A", "vertical", "green"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "vertical", "purple"),
        "D": Vehicle("D", "horizontal", "blue"), 
        "E": Vehicle("E", "vertical", "cyan"), 
        "F": Vehicle("F", "vertical", "green"),
        "G": Vehicle("G", "vertical", "yellow"), 
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "vertical", "blue"),
        "J": Vehicle("J", "horizontal", "grey"),
        "K": Vehicle("K", "vertical", "blue"),
        "L": Vehicle("L", "horizontal", "green"),
        "M": Vehicle("M", "vertical", "orange"),
        "N": Vehicle("N", "horizontal", "cyan"),
        "O": Vehicle("O", "horizontal", "green"), 
        "P": Vehicle("P", "vertical", "pink"),
        "Q": Vehicle("Q", "horizontal", "purple"),
        "S": Vehicle("S", "horizontal", "pink"), 
        "T": Vehicle("T", "vertical", "yellow"),
        "U": Vehicle("U", "vertical", "grey"), 
        "V": Vehicle("V", "horizontal", "purple"),
        "R": Vehicle("R", "horizontal", "red")
    }

def vehicles5():
    return {
        "A": Vehicle("A", "horizontal", "yellow"),
        "B": Vehicle("B", "vertical", "purple"),
        "C": Vehicle("C", "vertical", "blue"),
        "D": Vehicle("D", "vertical", "cyan"), 
        "E": Vehicle("E", "vertical", "green"),
        "F": Vehicle("F", "horizontal", "yellow"),
        "G": Vehicle("G", "vertical", "orange"), 
        "H": Vehicle("H", "horizontal", "blue"),
        "I": Vehicle("I", "horizontal", "cyan"),
        "J": Vehicle("J", "vertical", "orange"),
        "K": Vehicle("K", "horizontal", "green"),
        "L": Vehicle("L", "horizontal", "grey"),
        "M": Vehicle("M", "vertical", "cyan"),
        "N": Vehicle("N", "vertical", "purple"),
        "O": Vehicle("O", "horizontal", "green"), 
        "P": Vehicle("P", "vertical", "yellow"),
        "Q": Vehicle("Q", "horizontal", "blue"),
        "S": Vehicle("S", "vertical", "cyan"), 
        "T": Vehicle("T", "horizontal", "orange"),
        "U": Vehicle("U", "horizontal", "orange"), 
        "V": Vehicle("V", "vertical", "green"),
        "W": Vehicle("W", "vertical", "blue"),
        "X": Vehicle("X", "horizontal", "green"),
        "R": Vehicle("R", "horizontal", "red")
    }
    
import copy
import Queue

from rushvisual import *
from field import Field, Vehicle


def BFSearch(fieldsQueue, visited):
    solution = None
    while solution is None:
        field = fieldsQueue.get()
        # if field.tiles == [[0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1]]:
#             print field
        for x in range(len(field.vehicles)):
            vehicle = field.vehicles[x]
            moves = vehicle.getPossibleMoves(field)
            for move in moves:
                copyField = copy.deepcopy(field)
                copyVehicle = copyField.vehicles[x]
                copyVehicle.move(copyField, move[0], move[1], move[2])
                if not copyField in visited:
                    visited.add(copyField)
                    fieldsQueue.put(copyField)
                if copyVehicle.color == "red":
                    if copyVehicle.positions[-1] == copyField.exit:
                        print "FOUND SOLUTION"
                        print copyField
                        solution = copyField
    return solution

def field1():
    v1 = Vehicle([(1, 5), (1, 6)], "vertical", "orange")
    v2 = Vehicle([(2, 5), (3, 5)], "horizontal", "blue")
    v3 = Vehicle([(3, 1), (3, 2), (3, 3)], "vertical", "purple")
    v4 = Vehicle([(4, 4), (4, 5), (4, 6)], "vertical", "orange")
    v5 = Vehicle([(5, 6), (6, 6)], "horizontal", "green")
    v6 = Vehicle([(5, 4), (6, 4)], "horizontal", "orange")
    v7 = Vehicle([(4, 1), (5, 1)], "horizontal", "blue")
    v8 = Vehicle([(6, 1), (6, 2), (6, 3)], "vertical", "yellow")
    red = Vehicle([(4, 3), (5, 3)], "horizontal", "red")

    vehicles = [v1, v2, v3, v4, v5, v6, v7, v8, red]
    field = Field(6, vehicles)
    return field

def field2():
    v1 = Vehicle([(1, 5), (1, 6)], "vertical", "orange")
    v2 = Vehicle([(1, 4), (2, 4)], "horizontal", "green")
    v3 = Vehicle([(3, 4), (4, 4)], "horizontal", "blue")
    v4 = Vehicle([(4, 5), (4, 6)], "vertical", "light-blue")
    v5 = Vehicle([(5, 6), (6, 6)], "horizontal", "orange")
    v6 = Vehicle([(5, 5), (6, 5)], "horizontal", "green")
    v7 = Vehicle([(5, 3), (5, 4)], "vertical", "light-blue")
    v8 = Vehicle([(2, 2), (3, 2)], "horizontal", "orange")
    v9 = Vehicle([(4, 2), (5, 2)], "horizontal", "green")
    v10 = Vehicle([(6, 2), (6, 3), (6, 4)], "vertical", "yellow")
    v11 = Vehicle([(3, 1), (4, 1)], "horizontal", "blue")
    v12 = Vehicle([(5, 1), (6, 1)], "horizontal", "orange")
    red = Vehicle([(3, 3), (4, 3)], "horizontal", "red")

    vehicles = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, red]
    field = Field(6, vehicles)
    return field

def field3():
    v1 = Vehicle([(2, 1), (3, 1)], "horizontal", "blue")
    v2 = Vehicle([(4, 1), (5, 1), (6, 1)], "horizontal", "yellow")
    v3 = Vehicle([(2, 2), (3, 2)], "horizontal", "orange")
    v4 = Vehicle([(4, 2), (4, 3)], "vertical", "blue")
    v5 = Vehicle([(5, 2), (6, 2)], "horizontal", "green")
    v6 = Vehicle([(3, 3), (3, 4)], "vertical", "light-blue")
    v7 = Vehicle([(1, 4), (2, 4)], "horizontal", "green")
    v8 = Vehicle([(4, 4), (5, 4)], "horizontal", "blue")
    v9 = Vehicle([(6, 3), (6, 4)], "vertical", "light-blue")
    v10 = Vehicle([(1, 5), (1, 6)], "vertical", "orange")
    v11 = Vehicle([(3, 5), (3, 6)], "vertical", "green")
    v12 = Vehicle([(5, 5), (6, 5)], "horizontal", "green")
    red = Vehicle([(1, 3), (2, 3)], "horizontal", "red")

    vehicles = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, red]
    field = Field(6, vehicles)
    return field

if __name__ == "__main__":
    field = field2()
    queue = Queue.Queue()
    queue.put(field)
    BFSearch(queue, set([field]))
    anim = RushVisualisation(6, 6)
    # print field2()
#     print field3()

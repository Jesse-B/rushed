import copy
import games
import Queue

from field import Field, Vehicle
from rushvisual import RushVisualisation


def BFSearch(fieldsQueue, visited, vehicles):
    solution = None
    while solution is None:
        field = fieldsQueue.get()
        if field.tiles[field.exit] == "R":
            print "FOUND SOLUTION"
            print field
            solution = field
        movedVehicles = ""
        for tile in field.tiles:
            if tile != "0" and tile not in movedVehicles:
                vehicle = vehicles[tile]
                moves = vehicle.getPossibleMoves(field)
                for move in moves:
                    if not move.tiles in visited:
                        visited.add(move.tiles)
                        fieldsQueue.put(move)
                movedVehicles += tile
    return solution

if __name__ == "__main__":
    field = games.field1()
    vehicles = games.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(field)
    a = BFSearch(queue, set([field]), vehicles)
    RushVisualisation(6, vehicles.values(), a)

import copy
import games
import Queue

from field import Field, Vehicle
from rushvisual import RushVisualisation


def BFSearch(start, fieldsQueue, visited, vehicles):
    parent = {}
    solution = None
    while solution is None:
        field = fieldsQueue.get()
        if field.tiles[field.exit] == "R":
            solution = backtrace(parent, start, field)
        movedVehicles = ""
        for tile in field.tiles:
            if tile != "0" and tile not in movedVehicles:
                vehicle = vehicles[tile]
                moves = vehicle.getPossibleMoves(field)
                for move in moves:
                    if not move.tiles in visited:
                        parent[move] = field
                        visited.add(move.tiles)
                        fieldsQueue.put(move)
                movedVehicles += tile
    return solution

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

if __name__ == "__main__":
    field = games.field2()
    vehicles = games.vehicles2()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(field)
    a = BFSearch(field, queue, set([field]), vehicles)
    for state in a:
        RushVisualisation(6, vehicles.values(), state)
        print state
    

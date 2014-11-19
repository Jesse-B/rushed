import copy
import games
import Queue

from field import Field, Vehicle
from rushvisual import RushVisualisation


def BFSearch(start, fieldsQueue, visited):
    parent = {}
    solution = None
    while solution is None:
        field = fieldsQueue.get()
        if field.tiles[field.exit] == "R":
            solution = backtrace(parent, start, field.tiles)
        for x in range(field.length * field.length):
            if field.tiles[x] == "0":
                moves = field.getPossibleMovesForTile(x)
                for move in moves:
                    if not move in visited:
                        parent[move] = field.tiles
                        visited.add(move)
                        fieldsQueue.put(Field(move, field.length, field.horizontalCars, field.verticalCars))
    return solution

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

if __name__ == "__main__":
    field = games.field4()
    vehicles = games.vehicles4()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(field)
    a = BFSearch(field.tiles, queue, set([field]))
    for state in a:
        # RushVisualisation(6, vehicles.values(), state)
        print Field(state, field.length, field.horizontalCars, field.verticalCars)
    print "Steps:", len(a) - 1
    

import copy
import games
import Queue

from field import Field, Vehicle
from rushvisual import RushVisualisation


def BFSearch(startField, stateQueue, visited):
    parent = {}
    solution = None
    while solution is None:
        state = stateQueue.get()
        if state.tiles[field.exit] == "R":
            solution = backtrace(parent, startField, state.tiles)
        for x in range(state.length * state.length):
            if state.tiles[x] == "0":
                moves = state.getPossibleMovesForTile(x)
                for move in moves:
                    if not move in visited:
                        parent[move] = state.tiles
                        visited.add(move)
                        stateQueue.put(Field(move, state.length, state.horizontalCars, state.verticalCars))
    return solution

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

if __name__ == "__main__":
    field = games.field1()
    vehicles = games.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(field)
    import time
    now = time.time()
    a = BFSearch(field.tiles, queue, set([field]))
    print time.time() - now
    # for state in a:
        # RushVisualisation(6, vehicles.values(), state)
        # print Field(state, field.length, field.horizontalCars, field.verticalCars)
    # print "Steps:", len(a) - 1
    

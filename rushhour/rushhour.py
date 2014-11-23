import copy
import games
import Queue

from field import Field, Vehicle
from rushvisual import RushVisualisation


def BFSearch(field, startState, stateQueue, visited):
    parent = {}
    solution = None
    exit = field.exit
    numTiles = field.length * field.length
    while solution is None:
        state = stateQueue.get()
        if state[exit] == "R":
            solution = backtrace(parent, startState, state)
        field.tiles = state
        for x in xrange(numTiles):
            if field.tiles[x] == "0":
                moves = field.getPossibleMovesForTile(x)
                for move in moves:
                    if not move in visited:
                        parent[move] = state
                        visited.add(move)
                        stateQueue.put(move)
    return solution

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

if __name__ == "__main__":
    field = games.field1()
    # vehicles = games.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(field.tiles)
    import time
    now = time.time()
    a = BFSearch(field, field.tiles, queue, set([field.tiles]))
    print time.time() - now
    # for state in a:
        # RushVisualisation(6, vehicles.values(), state)
        # print Field(state, field.length, field.horizontalCars, field.verticalCars)
    # print "Steps:", len(a) - 1
    

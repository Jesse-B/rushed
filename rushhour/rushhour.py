import copy
import games
import Queue
import rushvisual

from field import Field
from rushvisual import RushVisualisation, Vehicle


def BFSearch(field, startState, stateQueue, visited):
    parent = {}
    solution = None
    exit = field.exit
    numTiles = field.length * field.length
    while solution is None:
        state = stateQueue.get()
        if state[exit] == "R":
            solution = backtrace(parent, startState, state)
        field.setTiles(state)
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

def AStarSearch(field, startState, stateQueue, visited):
    parent = {}
    solution = None
    exit = field.exit
    numTiles = field.length * field.length
    while solution is None:
        statePrio = stateQueue.get()
        state = statePrio[2]
        if state[exit] == "R":
            solution = backtrace(parent, startState, state)
        field.setTiles(state)
        for x in xrange(numTiles):
            if field.tiles[x] == "0":
                moves = field.getPossibleMovesForTile(x)
                for move in moves:
                    if not move in visited:
                        parent[move] = state
                        visited.add(move)
                        score = calculateScore(move, exit)
                        stateQueue.put((score + statePrio[1], statePrio[1] + 1, move))
    return solution

def calculateScore(state, exit):
    score = 0
    lastRPos = state.rfind("R")
    for x in range(lastRPos + 1, exit):
        score += 1
        if state[x] != "0":
            score += 1
    return score

if __name__ == "__main__":
    field = games.field1()
    vehicles = rushvisual.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)
    # queue = Queue.Queue()
#     queue.put(field.tiles)
    queue = Queue.PriorityQueue()
    queue.put((0, 0, field.tiles))
    import time
    now = time.time()
    # a = BFSearch(field, field.tiles, queue, set([field.tiles]))
    a = AStarSearch(field, field.tiles, queue, set([field.tiles]))
    print a
    print time.time() - now
    # for state in a:
    #     field = Field(state, 6, set(["B", "E", "F", "G", "R"]), set(["A", "C", "D", "H"]), vehicles)
    RushVisualisation(6, vehicles.values(), a)
        # print Field(state, field.length, field.horizontalCars, field.verticalCars)
    # print "Steps:", len(a) - 1
    

import time
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
    vehicles = field.vehicles
    while solution is None:
        statePrio = stateQueue.get()
        pathLength = statePrio[1]
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
                        score = calculateScore(move, exit, vehicles)
                        stateQueue.put((score + pathLength, pathLength + 1, move))
    return solution

def calculateScore(state, exit, vehicles):
    score = 0
    tilesToLeft = 1
    while True:
        score += 2
        tile = state[exit - tilesToLeft]
        if tile == "R":
            return score
        if tile != "0":
            if vehicles[tile] == 2:
                score += 1
            else:
                score += 2
        tilesToLeft += 1

if __name__ == "__main__":
    field = games.field4()
    vehicles = rushvisual.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)

    # Breadth First
    # queue = Queue.Queue()
#     queue.put(field.tiles)
#     now = time.time()
#     b = BFSearch(field, field.tiles, queue, set([field.tiles]))
#     print time.time() - now
#     # for state in b:
#         # RushVisualisation(6, vehicles.values(), state)
#         # print Field(state, field.length, field.horizontalCars, field.verticalCars)
#     print "Steps:", len(b) - 1

    # A*
    priorityQueue = Queue.PriorityQueue()
    priorityQueue.put((0, 0, field.tiles))
    now = time.time()
    a = AStarSearch(field, field.tiles, priorityQueue, set([field.tiles]))
    print time.time() - now
    print "Steps:", len(a) - 1

import time
import games
import collections
import Queue

from Tkinter import *
from timeit import Timer
from field import Field
from rushvisual import RushVisualisation, Vehicle, vehicles1, vehicles2, vehicles3, vehicles4


def BFSearch(field, startState, stateQueue, visited):
    parent = {}
    solution = None
    exit = field.exit
    numTiles = field.length * field.length
    while solution is None:
        state = stateQueue.popleft()
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
                        stateQueue.append(move)
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
    # field = games.field1()
    vehicles = vehicles1()
# #     # RushVisualisation(6, vehicles.values(), field)
# #
    vehicles_2 = vehicles2()
    vehicles_3 = vehicles3()
    # Breadth First
    queue = collections.deque()
    # queue.append(field.tiles)
    # print "Warming-up Breadth First algorithm for PyPy..."
    warmupTime = 0
    for x in range(10):
        queue.clear()
        field = games.field1()
        queue.append(field.tiles)
        now = time.time()
        BFSearch(field, field.tiles, queue, set([field.tiles]))
        warmupTime += time.time() - now
        if x == 9:
            queue.clear()
            field = games.field1()
            queue.append(field.tiles)
            # print "Done warming-up. Took %r seconds" % warmupTime
            now = time.time()
            # print "Solving puzzle 1:" 
            b = BFSearch(field, field.tiles, queue, set([field.tiles]))

            # Initialize a drawing surface
            master = Tk()
            w = Canvas(master, width=500, height=500)
            w.pack()
            master.update()

            # self.vis(self.fields, vehicles)

            button = Button(master, text="Visualisatie1", command=lambda: RushVisualisation(6, vehicles.values(), b, w, master))
            button.pack()


            # RushVisualisation(6, vehicles.values(), b)
            print "Aantal stappen: ", len(b)
            # print "Time:", time.time() - now, "seconds"
            # for state in b:
                # RushVisualisation(6, vehicles.values(), state)
                # print state
            # print "Steps:", len(b[0]) - 1
            queue.clear()
            field = games.field2()
            queue.append(field.tiles)
            now = time.time()
            # print "Solving puzzle 2:"
            
            b2 = BFSearch(field, field.tiles, queue, set([field.tiles]))
            button2 = Button(master, text="Visualisatie2", command=lambda: RushVisualisation(6, vehicles_2.values(), b2, w, master))
            button2.pack()

            # RushVisualisation(6, vehicles.values(), b)
            # print "Time:", time.time() - now, "seconds"
            # for state in b:
                # RushVisualisation(6, vehicles.values(), state)
                # print Field(state, field.length, field.horizontalCars, field.verticalCars)
            # print "Steps:", len(b[0]) - 1
            queue.clear()
            field = games.field3()
            queue.append(field.tiles)
            now = time.time()
            # print "Solving puzzle 1:"
            b3 = BFSearch(field, field.tiles, queue, set([field.tiles]))
            button3 = Button(master, text="Visualisatie3", command=lambda: RushVisualisation(6, vehicles_3.values(), b3, w, master))
            button3.pack()

    #         print "Time:", time.time() - now, "seconds"


    # field = games.field1()
#     queue.append(field.tiles)
#     now = time.time()
#     b = BFSearch(field, field.tiles, queue, set([field.tiles]))
#     print time.time() - now

    # # A*
    queue.clear()
    field4 = games.field4()
    priorityQueue = Queue.PriorityQueue()
    priorityQueue.put((0, 0, field.tiles))
    now = time.time()
    a4 = AStarSearch(field4, field4.tiles, priorityQueue, set([field4.tiles]))
    button4 = Button(master, text="Visualisatie4", command=lambda: RushVisualisation(9, vehicles_4.values(), a4, w, master))
    button4.pack()
    master.mainloop()

    # print time.time() - now
    # for state in a:
    #     field = Field(state, 6, set(["B", "E", "F", "G", "R"]), set(["A", "C", "D", "H"]), vehicles)
    # RushVisualisation(9, vehicles.values(), a)
        # print Field(state, field.length, field.horizontalCars, field.verticalCars)
    # print "Steps:", len(a) - 1

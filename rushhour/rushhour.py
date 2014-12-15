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
    numStates = 0
    while solution is None:
        numStates += 1
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
    return (solution, numStates)

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
    numStates = 0
    while solution is None:
        numStates += 1
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
    return (solution, numStates)

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

def runAlgorithmOnField(alg, field, algType):
    if algType == "BF":
        stateQueue = collections.deque()
        stateQueue.append(field.tiles)
    elif algType == "AStar":
        stateQueue = Queue.PriorityQueue()
        stateQueue.put((0, 0, field.tiles))
    now = time.time()
    solution = alg(field, field.tiles, stateQueue, set(field.tiles))
    time = time.time() - now
    return {"solution": solution[0], "numStates": solution[1], "time": time}

def warmUpForPuzzel(alg, field, algType):
    for x in range(10):
        runAlgorithmOnField(alg, field, algType)

if __name__ == "__main__":
    # field = games.field1()
    vehicles = vehicles1()
# #     # RushVisualisation(6, vehicles.values(), field)
# #
    vehicles_2 = vehicles2()
    vehicles_3 = vehicles3()
    vehicles_4 = vehicles4()
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
            w = Canvas(master, width=900, height=500)
            w.pack()
            master.update()
            w.grid(row=0, columnspan=5)

            button = Button(master, text="Visualisatie1", state=NORMAL, command=lambda: RushVisualisation(6, vehicles.values(), b[0], w, master))
            photo1 = PhotoImage(file = "images\game1.gif")
            button.config(image = photo1, width="120", height="120")
            button.grid(row=1)
            # button.pack()
            # button.place(x=700, y=100)
            

            print "Aantal stappen: ", len(b)

            queue.clear()
            field = games.field2()
            queue.append(field.tiles)
            now = time.time()
            # print "Solving puzzle 2:"
            
            b2 = BFSearch(field, field.tiles, queue, set([field.tiles]))
            button2 = Button(master, text="Visualisatie2", state=NORMAL, command=lambda: RushVisualisation(6, vehicles_2.values(), b2[0], w, master))
            photo2 = PhotoImage(file = "images\game2.gif")
            button2.config(image = photo2, width="120", height="120")
            button2.grid(row=1, column=1)

            # button2.pack()

 
            queue.clear()
            field = games.field3()
            queue.append(field.tiles)
            now = time.time()
            # print "Solving puzzle 1:"
            b3 = BFSearch(field, field.tiles, queue, set([field.tiles]))
            button3 = Button(master, text="Visualisatie3", state=NORMAL, command=lambda: RushVisualisation(6, vehicles_3.values(), b3[0], w, master))
            photo3 = PhotoImage(file = "images\game3.gif")
            button3.config(image = photo3, width="120", height="120")
            button3.grid(row=1, column=2)
            # button3.pack()


    # # A*
    queue.clear()
    field4 = games.field4()
    priorityQueue = Queue.PriorityQueue()
    priorityQueue.put((0, 0, field4.tiles))
    now = time.time()
    a4 = AStarSearch(field4, field4.tiles, priorityQueue, set([field4.tiles]))
    button4 = Button(master, text="Visualisatie4", state=NORMAL, command=lambda: RushVisualisation(9, vehicles_4.values(), a4[0], w, master))
    photo4 = PhotoImage(file = "images\game4.gif")
    button4.config(image = photo4, width="120", height="120")
    button4.grid(row=1, column=3)
    # button4.pack()
    

    # queue.clear()
    # field5 = games.field5()
    # priorityQueue = Queue.PriorityQueue()
    # priorityQueue.put((0, 0, field5.tiles))
    # now = time.time()
    # a5 = AStarSearch(field5, field5.tiles, priorityQueue, set([field5.tiles]))
    # button5 = Button(master, text="Visualisatie5", command=lambda: RushVisualisation(9, vehicles_5.values(), a5, w, master))
    # button5.grid(row=4, column=0)
    # button5.pack()


    # print time.time() - now
    # for state in a:
    #     field = Field(state, 6, set(["B", "E", "F", "G", "R"]), set(["A", "C", "D", "H"]), vehicles)
    # RushVisualisation(9, vehicles.values(), a)
        # print Field(state, field.length, field.horizontalCars, field.verticalCars)
    # print "Steps:", len(a) - 1




master.mainloop()

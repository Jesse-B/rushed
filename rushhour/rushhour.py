import time
import games
import collections
import Queue

from Tkinter import *
from timeit import Timer
from field import Field
from rushvisual import RushVisualisation, Vehicle, vehicles1, vehicles2, vehicles3, vehicles4, vehicles5, vehicles6, vehicles7


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
                        stateQueue.put((score + pathLength + 1, pathLength + 1, move))
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

<<<<<<< Updated upstream
def runAlgorithmOnField(alg, fieldFunc, algType):
    import time
    field = fieldFunc()
    if algType == "BF":
        stateQueue = collections.deque()
        stateQueue.append(field.tiles)
    elif algType == "AStar":
        stateQueue = Queue.PriorityQueue()
        stateQueue.put((0, 0, field.tiles))
=======
    

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
            w = Canvas(master, width=500, height=500)
            w.pack()
            master.update()

            # self.vis(self.fields, vehicles)

            button = Button(master, text="Visualisatie1", state=NORMAL, command=lambda: RushVisualisation(6, vehicles.values(), b, w, master))
            button.grid(row=0, column=0)
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
            button2 = Button(master, text="Visualisatie2", state=NORMAL, command=lambda: RushVisualisation(6, vehicles_2.values(), b2, w, master))
            button2.grid(row=1, column=0)
            button2.pack()

            # RushVisualisation(6, vehicles.values(), b)
            # print "Time:", time.time() - now, "seconds"
            # for state in b:
                # RushVisualisation(6, vehicles.values(), state)
                # print Field(state, field.length, field.horizontalCars, field.verticalCars)
            # print "Steps:", len(b[0]) - 1
            queue.clear()
            field = games.field4()
            queue.append(field.tiles)
            now = time.time()
            # print "Solving puzzle 1:"
            b3 = BFSearch(field, field.tiles, queue, set([field.tiles]))
            button3 = Button(master, text="Visualisatie3", state=NORMAL, command=lambda: RushVisualisation(6, vehicles_3.values(), b3, w, master))
            button3.grid(row=2, column=0)
            button3.pack()

            print "Time:", time.time() - now, "seconds"


 
    # field = games.field1()
#     queue.append(field.tiles)
#     now = time.time()
#     b = BFSearch(field, field.tiles, queue, set([field.tiles]))
#     print time.time() - now

    # # A*
    queue.clear()
    field4 = games.field4()
    priorityQueue = Queue.PriorityQueue()
    priorityQueue.put((0, 0, field4.tiles))
>>>>>>> Stashed changes
    now = time.time()
    solution = alg(field, field.tiles, stateQueue, set(field.tiles))
    time = time.time() - now
    return {"solution": solution[0], "numStates": solution[1], "time": time}

def warmUpForPuzzel(alg, fieldFunc, algType):
    for x in range(10):
        runAlgorithmOnField(alg, fieldFunc, algType)

def startUp(alg, field, algType, lenght, vehicles, canvas, the_object):
    theVis = RushVisualisation(lenght, vehicles, field().getCars(), canvas, the_object)
    if algType == "BF":
        warmUpForPuzzel(alg, field, algType)
    button5 = Button(the_object, text="Start algorithm", command=lambda: theVis.run(runAlgorithmOnField(alg, field, algType), button5))
    button5.grid(row=0, column=3, columnspan=5, sticky=S, pady=55)


if __name__ == "__main__":
    vehicles_1 = vehicles1()
    vehicles_2 = vehicles2()
    vehicles_3 = vehicles3()
    vehicles_4 = vehicles4()
    vehicles_5 = vehicles5()
    vehicles_6 = vehicles6()
    vehicles_7 = vehicles7()

    master = Tk()
    w = Canvas(master, width=650, height=500)
    w.pack()
    master.update()
    w.grid(row=0, columnspan=5)

    button = Button(master, text="Visualisatie1", state=NORMAL, command=lambda: startUp(BFSearch, games.field1, "BF", 6, vehicles_1.values(), w, master))
    photo1 = PhotoImage(file = "images/game1.gif")
    button.config(image = photo1, width="100", height="100")
    button.grid(row=1)

    button2 = Button(master, text="Visualisatie2", state=NORMAL, command=lambda: startUp(BFSearch, games.field2, "BF", 6, vehicles_2.values(), w, master))
    photo2 = PhotoImage(file = "images/game2.gif")
    button2.config(image = photo2, width="100", height="100")
    button2.grid(row=1, column=1)

    button3 = Button(master, text="Visualisatie3", state=NORMAL, command=lambda: startUp(BFSearch, games.field3, "BF", 6, vehicles_3.values(), w, master))
    photo3 = PhotoImage(file = "images/game3.gif")
    button3.config(image = photo3, width="100", height="100")
    button3.grid(row=1, column=2)

    button4 = Button(master, text="Visualisatie4", state=NORMAL, command=lambda: startUp(AStarSearch, games.field4, "AStar", 9, vehicles_4.values(), w, master))
    photo4 = PhotoImage(file = "images/game4.gif")
    button4.config(image = photo4, width="100", height="100")
    button4.grid(row=1, column=3)

    button5 = Button(master, text="Visualisatie5", state=NORMAL, command=lambda: startUp(AStarSearch, games.field5, "AStar", 9, vehicles_5.values(), w, master))
    photo5 = PhotoImage(file = "images/game5.gif")
    button5.config(image = photo5, width="100", height="100")
    button5.grid(row=1, column=4)

    button6 = Button(master, text="Visualisatie6", state=NORMAL, command=lambda: startUp(AStarSearch, games.field6, "AStar", 9, vehicles_6.values(), w, master))
    photo6 = PhotoImage(file = "images/game6.gif")
    button6.config(image = photo6, width="100", height="100")
    button6.grid(row=1, column=5)

    button7 = Button(master, text="Visualisatie7", state=NORMAL, command=lambda: startUp(AStarSearch, games.field7, "AStar", 12, vehicles_7.values(), w, master))
    photo7 = PhotoImage(file = "images/game7.gif")
    button7.config(image = photo7, width="100", height="100")
    button7.grid(row=1, column=6, padx=40)

master.mainloop()

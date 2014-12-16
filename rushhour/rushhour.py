import time
import games
import collections
import Queue

from Tkinter import *
from timeit import Timer
from field import Field
from rushvisual import RushVisualisation, Vehicle, vehicles1, vehicles2, vehicles3, vehicles4, vehicles5, vehicles6, vehicles7


def BFSearch(field, startState, stateQueue, visited, heuristic=None):
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

def AStarSearch(field, startState, stateQueue, visited, heuristic=None):
    parent = {}
    solution = None
    exit = field.exit
    fieldLen = field.length
    numTiles = fieldLen * fieldLen
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
                        score = heuristic(move, exit, vehicles, fieldLen)
                        stateQueue.put((score + pathLength + 1, pathLength + 1, move))
    return (solution, numStates)

def calculateScore4(state, exit, vehicles, fieldLen):
    score = 0
    tilesToLeft = 1
    while True:
        score += 1
        tile = state[exit - tilesToLeft]
        if tile == "R":
            return score
        if tile != "0":
            score += 1
        tilesToLeft += 1

def calculateScore5(state, exit, vehicles, fieldLen):
    return calculateScore51(state, exit, vehicles, fieldLen) + calculateScore52(state, exit, vehicles) + calculateScore53(state, exit, vehicles) + calculateScore54(state, exit, vehicles, fieldLen) + calculateScore55(state, exit, vehicles, fieldLen) + calculateScore56(state, exit, vehicles) + calculateScore57(state, exit, vehicles)

def calculateScore51(state, exit, vehicles, fieldLen):
    score = 0
    tilesDown = 0
    while True:
        tile = state[17 + (tilesDown * fieldLen)]
        if tile == "P":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesDown += 1

def calculateScore52(state, exit, vehicles):
    score = 0
    tilesToRight = 0
    while True:
        tile = state[63 + tilesToRight]
        if tile == "H":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesToRight += 1

def calculateScore53(state, exit, vehicles):
    score = 0
    tilesToRight = 0
    while True:
        tile = state[65 + tilesToRight]
        if tile == "L":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesToRight += 1

def calculateScore54(state, exit, vehicles, fieldLen):
    score = 0
    tilesUp = 0
    while True:
        tile = state[60 - (tilesUp * fieldLen)]
        if tile == "S":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesUp += 1

def calculateScore55(state, exit, vehicles, fieldLen):
    score = 0
    tilesUp = 0
    while True:
        tile = state[33 - (tilesUp * fieldLen)]
        if tile == "W":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesUp += 1

def calculateScore56(state, exit, vehicles):
    score = 0
    tilesToRight = 0
    while True:
        tile = state[15 + tilesToRight]
        if tile == "X":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesToRight += 1

def calculateScore57(state, exit, vehicles):
    score = 0
    tilesToRight = 0
    while True:
        tile = state[31 + tilesToRight]
        if tile == "T":
            return score
        score += 1
        if tile != "0":
            score += 1
        tilesToRight += 1


def runAlgorithmOnField(alg, fieldFunc, algType, heuristic=None):
    import time
    field = fieldFunc()
    if algType == "BF":
        stateQueue = collections.deque()
        stateQueue.append(field.tiles)
    elif algType == "AStar":
        stateQueue = Queue.PriorityQueue()
        stateQueue.put((0, 0, field.tiles))
    now = time.time()
    solution = alg(field, field.tiles, stateQueue, set(field.tiles), heuristic)
    time = time.time() - now
    return {"solution": solution[0], "numStates": solution[1], "time": time}

def warmUpForPuzzel(alg, fieldFunc, algType):
    for x in range(2):
        runAlgorithmOnField(alg, fieldFunc, algType)

def startUp(alg, field, algType, lenght, vehicles, canvas, the_object, heuristic=None):
    theVis = RushVisualisation(lenght, vehicles, field().getCars(), canvas, the_object)
    if algType == "BF":
        warmUpForPuzzel(alg, field, algType)
    button5 = Button(the_object, text="Start algorithm", command=lambda: theVis.run(runAlgorithmOnField(alg, field, algType, heuristic), button5))
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

    button4 = Button(master, text="Visualisatie4", state=NORMAL, command=lambda: startUp(AStarSearch, games.field4, "AStar", 9, vehicles_4.values(), w, master, calculateScore4))
    photo4 = PhotoImage(file = "images/game4.gif")
    button4.config(image = photo4, width="100", height="100")
    button4.grid(row=1, column=3)

    button5 = Button(master, text="Visualisatie5", state=NORMAL, command=lambda: startUp(AStarSearch, games.field5, "AStar", 9, vehicles_5.values(), w, master, calculateScore5))
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

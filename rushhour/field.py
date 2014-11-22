import Queue
import games

class Field(object):
    def __init__(self, tiles, length, horizontalCars, verticalCars):
        self.tiles = tiles
        self.length = length
        self.exit = (length * int(round(self.length / 2.0))) - 1
        self.horizontalCars = horizontalCars
        self.verticalCars = verticalCars

    def getPossibleMovesForTile(self, tilePos):
        row = tilePos / self.length
        moves = []

        leftPos = tilePos - 1
        if  row * self.length <= leftPos < (row + 1) * self.length:
            left = self.tiles[leftPos]
            if left in self.horizontalCars:
                leftPositions = [x for x in range(self.length * self.length) if self.tiles[x] == left]
                newTiles = self.tiles[:leftPositions[0]] + "0" + self.tiles[leftPositions[0] + 1:tilePos] + left + self.tiles[tilePos + 1:]
                moves.append(newTiles)
        upPos = tilePos - self.length
        if 0 <= upPos < len(self.tiles):
            up = self.tiles[upPos]
            if up in self.verticalCars:
                upPositions = [x for x in range(self.length * self.length) if self.tiles[x] == up]
                newTiles = self.tiles[:upPositions[0]] + "0" + self.tiles[upPositions[0] + 1:tilePos] + up + self.tiles[tilePos + 1:]
                moves.append(newTiles)
        rightPos = tilePos + 1
        if row * self.length <= rightPos < (row + 1) * self.length:
            right = self.tiles[rightPos]
            if right in self.horizontalCars:
                rightPositions = [x for x in range(self.length * self.length) if self.tiles[x] == right]
                newTiles = self.tiles[:tilePos] + right + self.tiles[tilePos + 1:rightPositions[-1]] + "0" + self.tiles[rightPositions[-1] + 1:]
                moves.append(newTiles)
        downPos = tilePos + self.length
        if 0 <= downPos < len(self.tiles):
            down = self.tiles[downPos]
            if down in self.verticalCars:
                downPositions = [x for x in range(self.length * self.length) if self.tiles[x] == down]
                newTiles = self.tiles[:tilePos] + down + self.tiles[tilePos + 1:downPositions[-1]] + "0" + self.tiles[downPositions[-1] + 1:]
                moves.append(newTiles)
        return moves

    def BFSearch(self, startField, stateQueue, visited):
        parent = {}
        solution = None
        while solution is None:
            state = stateQueue.get()
            if state[self.exit] == "R":
                solution = self.backtrace(parent, startField, state)
            self.tiles = state
            for x in range(self.length * self.length):
                if self.tiles[x] == "0":
                    moves = self.getPossibleMovesForTile(x)
                    for move in moves:
                        if not move in visited:
                            parent[move] = state
                            visited.add(move)
                            stateQueue.put(move)
        return solution

    def backtrace(awlf, parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def getCars(self):
        return self.tiles

    def __str__(self):
        rows = ""
        tileNum = self.length
        for row in range(len(self.tiles) / self.length):
            rows = rows + self.tiles[tileNum - self.length : tileNum] + '\n'
            tileNum += self.length
        return rows

    def __eq__(self, other):
        return self.tiles == other.tiles


class Vehicle(object):
    def __init__(self, name, orientation, color):
        self.name = name
        self.orientation = orientation
        self.color = color

    def getColor(self):
        return self.color

    def getCoor(self, field):
        self.len_tiles = len(field.tiles)
        rowx = {}
        xcoor = []
        coordinates = []
        for i in range(field.length):
            rowx[i+1] = field.tiles[(len(field.tiles)/field.length)*(i):(len(field.tiles)/field.length)*(i+1)]
            if self.name in rowx[i+1]:
                xcoor.append(i+1)

        for row in rowx.values():
            for i in range(field.length):
                if row[i] == self.name:
                    for coor in xcoor:
                        if (i+1,coor) not in coordinates:
                            coordinates.append((i+1,coor))

        miniy = coordinates[0][1]
        maxiy = coordinates[1][1]
        minix = coordinates[0][0]
        maxix = coordinates[1][0]
        if len(coordinates) == 3:

            for coor in coordinates:
                if self.orientation == "vertical":
                    if miniy > coor[1]:
                        miniy = coor[1]
                    if maxiy < coor[1]:
                        maxiy = coor[1]
                else:
                    if minix > coor[0]:
                        minix = coor[0]
                    if maxix < coor[0]:
                        maxix = coor[0]

        return (minix,miniy),(maxix,maxiy)


if __name__ == "__main__":
    field = games.field1()
    startState = field.tiles
    vehicles = games.vehicles1()
    # RushVisualisation(6, vehicles.values(), field)
    queue = Queue.Queue()
    queue.put(startState)
    import time
    now = time.time()
    a = field.BFSearch(startState, queue, set([startState]))
    print time.time() - now

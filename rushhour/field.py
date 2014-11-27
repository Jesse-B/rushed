class Field(object):
    def __init__(self, tiles, length, horizontalCars, verticalCars, vehicles):
        self.tiles = tiles
        self.row1 = tiles[0]
        self.row2 = tiles[1]
        self.row3 = tiles[2]
        self.row4 = tiles[3]
        self.row5 = tiles[4]
        self.row6 = tiles[5]
        self.length = length
        self.exit = (length * int(round(self.length / 2.0))) - 1
        self.horizontalCars = horizontalCars
        self.verticalCars = verticalCars
        self.vehicles = vehicles

    def updateTiles(self, tiles):
        self.tiles = tiles
        self.row1 = tiles[0]
        self.row2 = tiles[1]
        self.row3 = tiles[2]
        self.row4 = tiles[3]
        self.row5 = tiles[4]
        self.row6 = tiles[5]

    def getPossibleMovesForTile(self, tilePos):
        row = tilePos / self.length
        moves = set()

        leftPos = tilePos - 1
        if  row * self.length <= leftPos:
            left = self.tiles[leftPos]
            if left in self.horizontalCars:
                carLength = self.vehicles[left]
                firstPos = tilePos - carLength
                newTiles = self.tiles[:firstPos] + "0" + self.tiles[firstPos + 1:tilePos] + left + self.tiles[tilePos + 1:]
                moves.add(newTiles)
        upPos = tilePos - self.length
        if 0 <= upPos:
            up = self.tiles[upPos]
            if up in self.verticalCars:
                carLength = self.vehicles[up]
                firstPos = tilePos - (carLength * self.length)
                newTiles = self.tiles[:firstPos] + "0" + self.tiles[firstPos + 1:tilePos] + up + self.tiles[tilePos + 1:]
                moves.add(newTiles)
        rightPos = tilePos + 1
        if rightPos < (row + 1) * self.length:
            right = self.tiles[rightPos]
            if right in self.horizontalCars:
                carLength = self.vehicles[right]
                lastPos = tilePos + carLength
                newTiles = self.tiles[:tilePos] + right + self.tiles[tilePos + 1:lastPos] + "0" + self.tiles[lastPos + 1:]
                moves.add(newTiles)
        downPos = tilePos + self.length
        if downPos < len(self.tiles):
            down = self.tiles[downPos]
            if down in self.verticalCars:
                carLength = self.vehicles[down]
                lastPos = tilePos + (carLength * self.length)
                newTiles = self.tiles[:tilePos] + down + self.tiles[tilePos + 1:lastPos] + "0" + self.tiles[lastPos + 1:]
                moves.add(newTiles)
        return moves

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
    def __init__(self, name, orientation, length, color):
        self.name = name
        self.orientation = orientation
        self.length = length
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

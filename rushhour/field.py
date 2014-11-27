class Field(object):
    def __init__(self, tiles, length, horizontalCars, verticalCars, vehicles):
        self.tiles = tiles
        self.length = length
        self.exit = (length * int(round(self.length / 2.0))) - 1
        self.horizontalCars = horizontalCars
        self.verticalCars = verticalCars
        self.vehicles = vehicles

    def setTiles(self, tiles):
        self.tiles = tiles

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


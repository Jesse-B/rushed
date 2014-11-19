class Field(object):
    def __init__(self, tiles, length, horizontalCars, verticalCars):
        self.tiles = tiles
        self.length = length
        self.exit = (length * int(round(self.length / 2.0))) - 1
        self.horizontalCars = horizontalCars
        self.verticalCars = verticalCars

    def getValidNeighbour(self, pos, row=None):
        if row is None:
            if not 0 <= pos < len(self.tiles):
                return None
            if not self.tiles[pos] in self.verticalCars:
                return None
        else:
            if not row * self.length <= pos < (row + 1) * self.length:
                return None
            if not self.tiles[pos] in self.horizontalCars:
                return None
        return self.tiles[pos]

    def getPossibleMovesForTile(self, tilePos):
        row = tilePos / self.length
        moves = []

        left = self.getValidNeighbour(tilePos - 1, row)
        if left:
            leftPositions = [x for x in range(self.length * self.length) if self.tiles[x] == left]
            newTiles = self.tiles[:leftPositions[0]] + "0" + self.tiles[leftPositions[0] + 1:tilePos] + left + self.tiles[tilePos + 1:]
            moves.append(newTiles)
        up = self.getValidNeighbour(tilePos - self.length)
        if up:
            upPositions = [x for x in range(self.length * self.length) if self.tiles[x] == up]
            newTiles = self.tiles[:upPositions[0]] + "0" + self.tiles[upPositions[0] + 1:tilePos] + up + self.tiles[tilePos + 1:]
            moves.append(newTiles)
        right = self.getValidNeighbour(tilePos + 1, row)
        if right:
            rightPositions = [x for x in range(self.length * self.length) if self.tiles[x] == right]
            newTiles = self.tiles[:tilePos] + right + self.tiles[tilePos + 1:rightPositions[-1]] + "0" + self.tiles[rightPositions[-1] + 1:]
            moves.append(newTiles)
        down = self.getValidNeighbour(tilePos + self.length)
        if down:
            downPositions = [x for x in range(self.length * self.length) if self.tiles[x] == down]
            newTiles = self.tiles[:tilePos] + down + self.tiles[tilePos + 1:downPositions[-1]] + "0" + self.tiles[downPositions[-1] + 1:]
            moves.append(newTiles)
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
    v1 = Vehicle([(1, 1), (1, 2), (1, 3)], "vertical", "blue")
    v2 = Vehicle([(4, 3), (5, 3), (6, 3)], "horizontal", "yellow")
    v3 = Vehicle([(2, 6), (3, 6)], "horizontal", "green")
    v4 = Vehicle([(4, 5), (4, 6)], "vertical", "orange")
    vehicles = [v1, v2, v3, v4]
    field = Field(6, vehicles)
    print field
    for vehicle in field.vehicles:
        moves = vehicle.getPossibleMoves(field)
        for move in moves:
            vehicle.move(field, move[0], move[1], move[2])
    print field

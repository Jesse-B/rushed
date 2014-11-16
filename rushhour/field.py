class Field(object):
    def __init__(self, tiles, length):
        self.tiles = tiles
        self.length = length
        self.exit = (length * int(round(self.length / 2.0))) - 1

    def isTileEmpty(self, pos, row=None):
        if row is None:
            if not 0 <= pos < len(self.tiles):
                return False
        elif not row * self.length <= pos < (row + 1) * self.length:
            return False
        if self.tiles[pos] != "0":
            return False
        return True

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

    def getPossibleMoves(self, field):
        possibleMoves = []
        currentPositions = [i for i in range(len(field.tiles)) if field.tiles[i] == self.name]
        if self.orientation == "horizontal":
            row = currentPositions[0] / field.length
            leftTile = currentPositions[0] - 1
            if field.isTileEmpty(leftTile, row):
                tileToLeave = currentPositions[-1]
                newTiles = field.tiles[:leftTile] + self.name + field.tiles[leftTile + 1:tileToLeave] + "0" + field.tiles[tileToLeave + 1:]
                possibleMoves.append(Field(newTiles, field.length))

            rightTile = currentPositions[-1] + 1
            if field.isTileEmpty(rightTile, row):
                tileToLeave = currentPositions[0]
                newTiles = field.tiles[:tileToLeave] + "0" + field.tiles[tileToLeave + 1:rightTile] + self.name + field.tiles[rightTile + 1:]
                possibleMoves.append(Field(newTiles, field.length))

        if self.orientation == "vertical":
            upTile = currentPositions[0] - field.length
            if field.isTileEmpty(upTile):
                tileToLeave = currentPositions[-1]
                newTiles = field.tiles[:upTile] + self.name + field.tiles[upTile + 1:tileToLeave] + "0" + field.tiles[tileToLeave + 1:]
                possibleMoves.append(Field(newTiles, field.length))

            downTile = currentPositions[-1] + field.length
            if field.isTileEmpty(downTile):
                tileToLeave = currentPositions[0]
                newTiles = field.tiles[:tileToLeave] + "0" + field.tiles[tileToLeave + 1:downTile] + self.name + field.tiles[downTile + 1:]
                possibleMoves.append(Field(newTiles, field.length))

        return possibleMoves


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

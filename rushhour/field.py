class Field(object):
    def __init__(self, length):
        self.tiles = [[0 for x in range(length)] for x in range(length)]

    def modifyTile(self, pos, status):
        if status == "occupy":
            self.tiles[pos[1] - 1][pos[0] - 1] = 1
        elif status == "leave":
            self.tiles[pos[1] - 1][pos[0] - 1] = 0

    def isTileEmpty(self, pos):
        try:
            if self.tiles[pos[1] - 1][pos[0] - 1] == 1:
                return False
        except IndexError:
            return False
        return True

    def __str__(self):
        rows = ""
        for row in self.tiles:
            rows = rows + str(row) + '\n'
        return rows

    def __eq__(self, other):
       return self.tiles == other.tiles


class Vehicle(object):
    def __init__(self, field, positions, orientation, color):
        self.field = field
        self.positions = positions
        self.orientation = orientation
        self.color = color

        for pos in self.positions:
            self.field.modifyTile(pos, "occupy")

    def getPossibleMoves(self):
        possibleMoves = []
        if self.orientation == "horizontal":
            leftTile = (self.positions[0][0] - 1, self.positions[0][1])
            if self.field.isTileEmpty(leftTile):
                tileToLeave = self.positions[-1]
                possibleMoves.append((tileToLeave, leftTile, "left"))
            rightTile = (self.positions[-1][0] + 1, self.positions[-1][1])
            if self.field.isTileEmpty(rightTile):
                tileToLeave = self.positions[0]
                possibleMoves.append((tileToLeave, rightTile, "right"))

        if self.orientation == "vertical":
            upTile = (self.positions[0][0], self.positions[0][1] - 1)
            if self.field.isTileEmpty(upTile):
                tileToLeave = self.positions[-1]
                possibleMoves.append((tileToLeave, upTile, "up"))
            downTile = (self.positions[-1][0], self.positions[-1][1] + 1)
            if self.field.isTileEmpty(downTile):
                tileToLeave = self.positions[0]
                possibleMoves.append((tileToLeave, downTile, "down"))

        return possibleMoves

    def move(self, tileToLeave, tileToOccupy, direction):
        self.field.modifyTile(tileToLeave, "leave")
        self.field.modifyTile(tileToOccupy, "occupy")

        self.positions.remove(tileToLeave)
        if direction == "left" or direction == "up":
            self.positions.insert(0, tileToOccupy)
        elif direction == "right" or direction == "down":
            self.positions.append(tileToOccupy)


if __name__ == "__main__":
    field = Field(6)
    field2 = Field(6)
    print field == field2
    print field
    v1 = Vehicle(field, [(1, 1), (1, 2), (1, 3)], "vertical", "blue")
    v2 = Vehicle(field, [(4, 3), (5, 3), (6, 3)], "horizontal", "yellow")
    v3 = Vehicle(field, [(2, 6), (3, 6)], "horizontal", "green")
    print field
    v2Moves = v2.getPossibleMoves()
    for move in v2Moves:
        v2.move(move[0], move[1], move[2])
    print field

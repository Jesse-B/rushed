class Field(object):
    def __init__(self, length, vehicles):
        self.tiles = [[0 for x in range(length)] for x in range(length)]
        self.exit = (length, int(round(length / 2.0)))
        self.vehicles = vehicles

        for vehicle in self.vehicles:
            vehicle.insertVehicleInField(self)

    def modifyTile(self, pos, status):
        if status == "occupy":
            self.tiles[pos[1] - 1][pos[0] - 1] = 1
        elif status == "leave":
            self.tiles[pos[1] - 1][pos[0] - 1] = 0

    def isTileEmpty(self, pos):
        try:
            if self.tiles[pos[1] - 1][pos[0] - 1] == 1 or pos[0] < 1 or pos[1] < 1:
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

    def __hash__(self):
        return hash(str(self.tiles))


class Vehicle(object):
    def __init__(self, positions, orientation, color):
        self.positions = positions
        self.orientation = orientation
        self.color = color

    def insertVehicleInField(self, field):
        for pos in self.positions:
            field.modifyTile(pos, "occupy")

    def getPossibleMoves(self, field):
        possibleMoves = []
        if self.orientation == "horizontal":
            leftTile = (self.positions[0][0] - 1, self.positions[0][1])
            if field.isTileEmpty(leftTile):
                tileToLeave = self.positions[-1]
                possibleMoves.append((tileToLeave, leftTile, "left"))
            rightTile = (self.positions[-1][0] + 1, self.positions[-1][1])
            if field.isTileEmpty(rightTile):
                tileToLeave = self.positions[0]
                possibleMoves.append((tileToLeave, rightTile, "right"))

        if self.orientation == "vertical":
            upTile = (self.positions[0][0], self.positions[0][1] - 1)
            if field.isTileEmpty(upTile):
                tileToLeave = self.positions[-1]
                possibleMoves.append((tileToLeave, upTile, "up"))
            downTile = (self.positions[-1][0], self.positions[-1][1] + 1)
            if field.isTileEmpty(downTile):
                tileToLeave = self.positions[0]
                possibleMoves.append((tileToLeave, downTile, "down"))

        return possibleMoves

    def move(self, field, tileToLeave, tileToOccupy, direction):
        field.modifyTile(tileToLeave, "leave")
        field.modifyTile(tileToOccupy, "occupy")

        self.positions.remove(tileToLeave)
        if direction == "left" or direction == "up":
            self.positions.insert(0, tileToOccupy)
        elif direction == "right" or direction == "down":
            self.positions.append(tileToOccupy)


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

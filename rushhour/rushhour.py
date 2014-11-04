class Field(object):
    def __init__(self, length):
        self.tiles = [[0 for x in range(length)] for x in range(length)]

    def modifyTiles(self, dest, source=None):
        if source:
            for pos in source:
                self.tiles[pos[1] - 1][pos[0] - 1] = 0
        for pos in dest:
            self.tiles[pos[1] - 1][pos[0] - 1] = 1

    def areTilesEmpty(self, positions):
        for pos in positions:
            if self.tiles[pos[1] - 1][pos[0] - 1] == 1:
                raise Exception
        return True

    def arePositionsValid(self, positions, vehicleOrientation):
        for pos in positions:
            # check if position in field
            try:
                self.tiles[pos[1] - 1][pos[0] - 1]
            except IndexError:
                raise Exception

            # check if tile is empty
            if not self.areTilesEmpty(positions):
                raise Exception

        # check if positions on one line and same orientation
        if vehicleOrientation == "horizontal":
            yPositions = [pos[1] for pos in positions]
            if not len(set(yPositions)) == 1:
                raise Exception
        elif vehicleOrientation == "vertical":
            xPositions = [pos[0] for pos in positions]
            if not len(set(xPositions)) == 1:
                raise Exception
        return True

    def __str__(self):
        rows = ""
        for row in self.tiles:
            rows = rows + str(row) + '\n'
        return rows


class Vehicle(object):
    def __init__(self, field, positions, orientation, color):
        self.field = field
        self.positions = positions
        self.length = len(positions)
        self.orientation = orientation
        self.color = color

        if self.field.arePositionsValid(self.positions, self.orientation):
            self.field.modifyTiles(self.positions)

    def moveTo(self, positions):
        if self.orientation == "horizontal":
            steps = positions[0][0] - self.positions[0][0]
        else:
            steps = positions[0][1] - self.positions[0][1]

        if self.isMoveValid(positions, steps):
            self.field.modifyTiles(positions, self.positions)
            self.setPositions(positions)

    def isMoveValid(self, positions, steps):
        if not self.field.arePositionsValid(positions, self.orientation):
            # check if tiles in between are also empty
            raise Exception
        return True

    def setPositions(self, positions):
        self.positions = positions


if __name__ == "__main__":
    field = Field(6)
    print field
    v1 = Vehicle(field, [(1, 1), (1, 2), (1, 3)], "vertical", "blue")
    v2 = Vehicle(field, [(4, 3), (5, 3), (6, 3)], "horizontal", "yellow")
    v3 = Vehicle(field, [(2, 6), (3, 6)], "horizontal", "green")
    print field
    v3.moveTo([(5,6), (6,6)])
    print field
    try:
        v2.moveTo([(4, 4), (5, 4), (6, 4)])
        print "Should raise exception, but didn't."
    except Exception:
        print "Succesfully raised exception."

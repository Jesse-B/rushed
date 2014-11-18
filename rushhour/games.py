from field import Field, Vehicle

def field1():
    tiles = "00CGGH00C00H00CRRH000DFFABBD00A00DEE"
    # 00CGGH
    # 00C00H
    # 00CRRH
    # 000DFF
    # ABBD00
    # A00DEE
    field = Field(tiles, 6)
    return field

def vehicles1():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "blue"),
        "C": Vehicle("C", "vertical", "purple"),
        "D": Vehicle("D", "vertical", "orange"),
        "E": Vehicle("E", "horizontal", "green"),
        "F": Vehicle("F", "horizontal", "orange"),
        "G": Vehicle("G", "horizontal", "blue"),
        "H": Vehicle("H", "vertical", "yellow"),
        "R": Vehicle("R", "horizontal", "red"),
    }

def field2():
    v1 = Vehicle([(1, 5), (1, 6)], "vertical", "orange")
    v2 = Vehicle([(1, 4), (2, 4)], "horizontal", "green")
    v3 = Vehicle([(3, 4), (4, 4)], "horizontal", "blue")
    v4 = Vehicle([(4, 5), (4, 6)], "vertical", "blue") # lightblue
    v5 = Vehicle([(5, 6), (6, 6)], "horizontal", "orange")
    v6 = Vehicle([(5, 5), (6, 5)], "horizontal", "green")
    v7 = Vehicle([(5, 3), (5, 4)], "vertical", "blue") # lightblue
    v8 = Vehicle([(2, 2), (3, 2)], "horizontal", "orange")
    v9 = Vehicle([(4, 2), (5, 2)], "horizontal", "green")
    v10 = Vehicle([(6, 2), (6, 3), (6, 4)], "vertical", "yellow")
    v11 = Vehicle([(3, 1), (4, 1)], "horizontal", "blue")
    v12 = Vehicle([(5, 1), (6, 1)], "horizontal", "orange")
    red = Vehicle([(3, 3), (4, 3)], "horizontal", "red")

    vehicles = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, red]
    field = Field(6, vehicles)
    # anim = RushVisualisation(6, 6, vehicles)
    # print anim
    return field

def field3():
    v1 = Vehicle([(2, 1), (3, 1)], "horizontal", "blue")
    v2 = Vehicle([(4, 1), (5, 1), (6, 1)], "horizontal", "yellow")
    v3 = Vehicle([(2, 2), (3, 2)], "horizontal", "orange")
    v4 = Vehicle([(4, 2), (4, 3)], "vertical", "blue")
    v5 = Vehicle([(5, 2), (6, 2)], "horizontal", "green")
    v6 = Vehicle([(3, 3), (3, 4)], "vertical", "blue") # lightblue
    v7 = Vehicle([(1, 4), (2, 4)], "horizontal", "green")
    v8 = Vehicle([(4, 4), (5, 4)], "horizontal", "blue")
    v9 = Vehicle([(6, 3), (6, 4)], "vertical", "blue") # lightblue
    v10 = Vehicle([(1, 5), (1, 6)], "vertical", "orange")
    v11 = Vehicle([(3, 5), (3, 6)], "vertical", "green")
    v12 = Vehicle([(5, 5), (6, 5)], "horizontal", "green")
    red = Vehicle([(1, 3), (2, 3)], "horizontal", "red")

    vehicles = [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, red]
    field = Field(6, vehicles)
    # anim = RushVisualisation(6, 6, vehicles)
    # print anim
    return field

if __name__ == "__main__":
    field1()
#    field2()
##    field3()

from field import Field, Vehicle


def field1():
    field = Field(6)
    v1 = Vehicle(field, [(1, 5), (1, 6)], "vertical", "orange")
    v2 = Vehicle(field, [(2, 5), (3, 5)], "horizontal", "blue")
    v3 = Vehicle(field, [(3, 3), (3, 2), (3, 1)], "vertical", "purple")
    v4 = Vehicle(field, [(4, 6), (4, 5), (4, 4)], "vertical", "orange")
    v5 = Vehicle(field, [(5, 6), (6, 6)], "horizontal", "green")
    v6 = Vehicle(field, [(5, 4), (6, 4)], "horizontal", "orange")
    v7 = Vehicle(field, [(4, 1), (5, 1)], "horizontal", "blue")
    v8 = Vehicle(field, [(6, 3), (6, 2), (6, 1)], "vertical", "Yellow")

    red = Vehicle(field, [(4, 3), (5, 3)], "horizontal", "red")
    return field

def field2():
    field = Field(6)
    v1 = Vehicle(field, [(1, 6), (1, 5)], "vertical", "orange")
    v2 = Vehicle(field, [(1, 4), (2, 4)], "horizontal", "green")
    v3 = Vehicle(field, [(3, 4), (4, 4)], "horizontal", "blue")
    v4 = Vehicle(field, [(4, 6), (4, 5)], "vertical", "light-blue")
    v5 = Vehicle(field, [(5, 6), (6, 6)], "horizontal", "orange")
    v6 = Vehicle(field, [(5, 5), (6, 5)], "horizontal", "green")
    v7 = Vehicle(field, [(5, 4), (5, 3)], "vertical", "light-blue")
    v8 = Vehicle(field, [(2, 2), (3, 2)], "horizontal", "orange")
    v9 = Vehicle(field, [(4, 2), (5, 2)], "horizontal", "green")
    v10 = Vehicle(field, [(6, 4), (6, 3), (6, 2)], "vertical", "yellow")
    v11 = Vehicle(field, [(3, 1), (4, 1)], "horizontal", "blue")
    v12 = Vehicle(field, [(5, 1), (6, 1)], "horizontal", "orange")

    red = Vehicle(field, [(3, 3), (4, 3)], "horizontal", "red")
    return field

def field3():
    field = Field(6)
    v1 = Vehicle(field, [(2, 1), (3, 1)], "horizontal", "blue")
    v2 = Vehicle(field, [(4, 1), (5, 1), (6, 1)], "horizontal", "yellow")
    v3 = Vehicle(field, [(2, 2), (3, 2)], "horizontal", "orange")
    v4 = Vehicle(field, [(4, 2), (4, 3)], "vertical", "blue")
    v5 = Vehicle(field, [(5, 2), (6, 2)], "horizontal", "green")
    v6 = Vehicle(field, [(3, 3), (3, 4)], "vertical", "light-blue")
    v7 = Vehicle(field, [(1, 4), (2, 4)], "horizontal", "green")
    v8 = Vehicle(field, [(4, 4), (5, 4)], "horizontal", "blue")
    v9 = Vehicle(field, [(6, 3), (6, 4)], "vertical", "light-blue")
    v10 = Vehicle(field, [(1, 5), (1, 6)], "vertical", "orange")
    v11 = Vehicle(field, [(3, 5), (3, 6)], "vertical", "green")
    v12 = Vehicle(field, [(5, 5), (6, 5)], "horizontal", "green")

    red = Vehicle(field, [(1, 3), (2, 3)], "horizontal", "red")
    return field

if __name__ == "__main__":
    print field1()
    print field2()
    print field3()

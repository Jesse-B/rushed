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
        "R": Vehicle("R", "horizontal", "red")
    }
    
def field2():
    tiles = "00KKLL0HHIIJ00RRGJBBCCGJA00DFFA00DEE"
#    00KKLL
#    0HHIIJ
#    00RRGJ
#    BBCCGJ
#    A00DFF
#    A00DEE
    field = Field(tiles, 6)
    return field
    
def vehicles2():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "green"),
        "C": Vehicle("C", "horizontal", "blue"),
        "D": Vehicle("D", "vertical", "blue"), #light blue
        "E": Vehicle("E", "horizontal", "orange"),
        "F": Vehicle("F", "horizontal", "green"),
        "G": Vehicle("G", "vertical", "blue"), # lightblue
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "horizontal", "green"),
        "J": Vehicle("J", "vertical", "yellow"),
        "K": Vehicle("K", "horizontal", "blue"),
        "L": Vehicle("L", "horizontal", "orange"),
        "R": Vehicle("R", "horizontal", "red")
        }

def field3():
    tiles = "0AABBB0CCDEERRFD0IGGFHHIJ0K0LLJ0K000"
#    0AABBB
#    0CCDEE
#    RRFD0I
#    GGFHHI
#    J0K0LL
#    J0K000
    field = Field(tiles, 6)
    return field
    
def vehicles3():
    return {
        "A": Vehicle("A", "horizontal", "blue"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "horizontal", "orange"),
        "D": Vehicle("D", "vertical", "blue"), 
        "E": Vehicle("E", "horizontal", "green"),
        "F": Vehicle("F", "vertical", "blue"), # lightblue
        "G": Vehicle("G", "horizontal", "green"), 
        "H": Vehicle("H", "horizontal", "blue"),
        "I": Vehicle("I", "vertical", "blue"), # lightblue
        "J": Vehicle("J", "vertical", "orange"),
        "K": Vehicle("K", "vertical", "green"),
        "L": Vehicle("L", "horizontal", "green"),
        "R": Vehicle("R", "horizontal", "red")
    }

if __name__ == "__main__":
    field1()
#    field2()
##    field3()

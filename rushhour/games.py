from field import Field, Vehicle

def grandmasterField():
    tiles = "KKKADGJBBADGJ0RRDGCCL0000EL0II0EHHFF"
    # KKKADG
    # JBBADG
    # J0RRDG
    # CCL000
    # 0EL0II
    # 0EHHFF

    field = Field(tiles, 6, "BCFHIKR", "ADEGJL")
    return field

def grandmasterVehicles():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "green"),
        "C": Vehicle("C", "horizontal", "blue"),
        "D": Vehicle("D", "vertical", "cyan"),
        "E": Vehicle("E", "vertical", "orange"),
        "F": Vehicle("F", "horizontal", "green"),
        "G": Vehicle("G", "vertical", "cyan"),
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "horizontal", "green"),
        "J": Vehicle("J", "vertical", "yellow"),
        "K": Vehicle("K", "horizontal", "blue"),
        "L": Vehicle("L", "vertical", "orange"),
        "R": Vehicle("R", "horizontal", "red")
    }

def field1():
    tiles = "00CGGH00C00H00CRRH000DFFABBD00A00DEE"
    # 00CGGH
#     00C00H
#     00CRRH
#     000DFF
#     ABBD00
#     A00DEE
    vehicles = {
        "A": 2,
        "B": 2,
        "C": 3,
        "D": 3,
        "E": 2,
        "F": 2,
        "G": 2,
        "H": 3,
        "R": 2
    }
    field = Field(tiles, 6, set(["B", "E", "F", "G", "R"]), set(["A", "C", "D", "H"]), vehicles)
    return field

# def vehicles1():
#     return {
#         "A": Vehicle("A", "vertical", 2, "orange"),
#         "B": Vehicle("B", "horizontal", 2, "blue"),
#         "C": Vehicle("C", "vertical", 3, "purple"),
#         "D": Vehicle("D", "vertical", 3, "orange"),
#         "E": Vehicle("E", "horizontal", 2, "green"),
#         "F": Vehicle("F", "horizontal", 2, "orange"),
#         "G": Vehicle("G", "horizontal", 2, "blue"),
#         "H": Vehicle("H", "vertical", 3, "yellow"),
#         "R": Vehicle("R", "horizontal", 2, "red")
#     }
    
def field2():
    tiles = "00KKLL0HHIIJ00RRGJBBCCGJA00DFFA00DEE"
#    00KKLL
#    0HHIIJ
#    00RRGJ
#    BBCCGJ
#    A00DFF
#    A00DEE
    field = Field(tiles, 6, "BCEFHIKLR", "ADGJ")
    return field
    
def vehicles2():
    return {
        "A": Vehicle("A", "vertical", "orange"),
        "B": Vehicle("B", "horizontal", "green"),
        "C": Vehicle("C", "horizontal", "blue"),
        "D": Vehicle("D", "vertical", "cyan"),
        "E": Vehicle("E", "horizontal", "orange"),
        "F": Vehicle("F", "horizontal", "green"),
        "G": Vehicle("G", "vertical", "cyan"),
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
    field = Field(tiles, 6, "ABCEGHLR", "DFIJK")
    return field
    
def vehicles3():
    return {
        "A": Vehicle("A", "horizontal", "blue"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "horizontal", "orange"),
        "D": Vehicle("D", "vertical", "blue"), 
        "E": Vehicle("E", "horizontal", "green"),
        "F": Vehicle("F", "vertical", "cyan"), 
        "G": Vehicle("G", "horizontal", "green"), 
        "H": Vehicle("H", "horizontal", "blue"),
        "I": Vehicle("I", "vertical", "cyan"), 
        "J": Vehicle("J", "vertical", "orange"),
        "K": Vehicle("K", "vertical", "green"),
        "L": Vehicle("L", "horizontal", "green"),
        "R": Vehicle("R", "horizontal", "red")
    }
    
def field4():
    tiles = "ABBB0U000A00C0UVVV000C0U00TDD0C0SSSTERRF0000TE0GF0QQQPHHGKLL00PI0GKM000PIJJJMNNOO"
    
#    ABBB0U000
#    A00C0UVVV
#    000C0U00T
#    DD0C0SSST
#    ERRF0000T
#    E0GF0QQQP
#    HHGKLL00P
#    I0GKM000P
#    IJJJMNNOO
    
    field = Field(tiles, 9, "BDHJLNOQSVR", "ACEFGIKMPTU")
    return field
    
def vehicles4():
    return {
        "A": Vehicle("A", "vertical", "green"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "vertical", "purple"),
        "D": Vehicle("D", "horizontal", "blue"), 
        "E": Vehicle("E", "vertical", "cyan"), 
        "F": Vehicle("F", "vertical", "green"),
        "G": Vehicle("G", "vertical", "yellow"), 
        "H": Vehicle("H", "horizontal", "orange"),
        "I": Vehicle("I", "vertical", "blue"),
        "J": Vehicle("J", "horizontal", "grey"),
        "K": Vehicle("K", "vertical", "blue"),
        "L": Vehicle("L", "horizontal", "green"),
        "M": Vehicle("M", "vertical", "orange"),
        "N": Vehicle("N", "horizontal", "cyan"),
        "O": Vehicle("O", "horizontal", "green"), 
        "P": Vehicle("P", "vertical", "pink"),
        "Q": Vehicle("Q", "horizontal", "purple"),
        "S": Vehicle("S", "horizontal", "pink"), 
        "T": Vehicle("T", "vertical", "yellow"),
        "U": Vehicle("U", "vertical", "grey"), 
        "V": Vehicle("V", "horizontal", "purple"),
        "R": Vehicle("R", "horizontal", "red")
    }
    
def field5():
    tiles = "AAAB0VW00000B0VWXX000BUUS000000QQSTT00FFFNRRPC0G00N00PC0GKKNOOPDEHHJLLLMDEIIJ000M"
    
#    AAAB0VW00
#    000B0VWXX   
#    000BUUS00
#    0000QQSTT
#    00FFFNRRP
#    C0G00N00P
#    C0GKKNOOP
#    DEHHJLLLM
#    DEIIJ000M
    
    field = Field(tiles, 9, "AFHIKLOQTUXR", "BCDEGJMNPSVW")
    return field

def vehicles5():
    return {
        "A": Vehicle("A", "horizontal", "yellow"),
        "B": Vehicle("B", "vertical", "purple"),
        "C": Vehicle("C", "vertical", "blue"),
        "D": Vehicle("D", "vertical", "cyan"), 
        "E": Vehicle("E", "vertical", "green"),
        "F": Vehicle("F", "horizontal", "yellow"),
        "G": Vehicle("G", "vertical", "orange"), 
        "H": Vehicle("H", "horizontal", "blue"),
        "I": Vehicle("I", "horizontal", "cyan"),
        "J": Vehicle("J", "vertical", "orange"),
        "K": Vehicle("K", "horizontal", "green"),
        "L": Vehicle("L", "horizontal", "grey"),
        "M": Vehicle("M", "vertical", "cyan"),
        "N": Vehicle("N", "vertical", "purple"),
        "O": Vehicle("O", "horizontal", "green"), 
        "P": Vehicle("P", "vertical", "yellow"),
        "Q": Vehicle("Q", "horizontal", "blue"),
        "S": Vehicle("S", "vertical", "cyan"), 
        "T": Vehicle("T", "horizontal", "orange"),
        "U": Vehicle("U", "horizontal", "orange"), 
        "V": Vehicle("V", "vertical", "green"),
        "W": Vehicle("W", "vertical", "blue"),
        "X": Vehicle("X", "horizontal", "green"),
        "R": Vehicle("R", "horizontal", "red")
    }
    
    
def field6():
    tiles = "AABBM00Z0CDDDMOOZ0C0EENP0YY00KLNPXXXRRKL000000G0LQQVVWFGJJSUUUWF0IISTT0WFHHHS0000"
    
#    AABBM00Z0
#    CDDDMOOZ0
#    C0EENP0YY
#    00KLNPXXX
#    RRKL00000
#    0G0LQQVVW
#    FGJJSUUUW
#    F0IISTT0W
#    FHHHS0000
    
    field = Field(tiles, 9, "ABDEHIJOQTUVXYR", "CFGKLMNPSWZ")
    return field
    
def vehicles6():
    return {
        "A": Vehicle("A", "horizontal", "blue"),
        "B": Vehicle("B", "horizontal", "cyan"),
        "C": Vehicle("C", "vertical", "cyan"),
        "D": Vehicle("D", "horizontal", "yellow"), 
        "E": Vehicle("E", "horizontal", "green"), 
        "F": Vehicle("F", "vertical", "purple"),
        "G": Vehicle("G", "vertical", "orange"), 
        "H": Vehicle("H", "horizontal", "yellow"),
        "I": Vehicle("I", "horizontal", "blue"),
        "J": Vehicle("J", "horizontal", "green"),
        "K": Vehicle("K", "vertical", "blue"),
        "L": Vehicle("L", "vertical", "yellow"),
        "M": Vehicle("M", "vertical", "green"),
        "N": Vehicle("N", "vertical", "orange"),
        "O": Vehicle("O", "horizontal", "orange"), 
        "P": Vehicle("P", "vertical", "orange"),
        "Q": Vehicle("Q", "horizontal", "cyan"),
        "S": Vehicle("S", "vertical", "grey"), 
        "T": Vehicle("T", "horizontal", "green"),
        "U": Vehicle("U", "horizontal", "yellow"), 
        "V": Vehicle("V", "horizontal", "orange"),
        "W": Vehicle("W", "vertical", "purple"),
        "X": Vehicle("X", "horizontal", "grey"),
        "Y": Vehicle("Y", "horizontal", "green"),
        "Z": Vehicle("Z", "vertical", "blue"), 
        "R": Vehicle("R", "horizontal", "red")
    }
  
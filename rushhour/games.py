from field import Field

def grandmasterField():
    tiles = "KKKADGJBBADGJ0RRDGCCL0000EL0II0EHHFF"
    # KKKADG
#     JBBADG
#     J0RRDG
#     CCL000
#     0EL0II
#     0EHHFF

    vehicles = {
        "A": 2,
        "B": 2,
        "C": 2,
        "D": 3,
        "E": 2,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 2,
        "J": 2,
        "K": 3,
        "L": 2,
        "R": 2
    }

    field = Field(tiles, 6, set(["B", "C", "F", "H", "I", "K", "R"]), set(["A", "D", "E", "G", "J", "L"]), vehicles)
    return field

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
    # 00KKLL
#     0HHIIJ
#     00RRGJ
#     BBCCGJ
#     A00DFF
#     A00DEE

    vehicles = {
        "A": 2,
        "B": 2,
        "C": 2,
        "D": 2,
        "E": 2,
        "F": 2,
        "G": 2,
        "H": 2,
        "I": 2,
        "J": 3,
        "K": 2,
        "L": 2,
        "R": 2
    }

    field = Field(tiles, 6, set(["B","C","E","F","H","I","K","L","R"]), set(["A","D","G","J"]), vehicles)
    return field
    
# def vehicles2():
#     return {
#         "A": Vehicle("A", "vertical", "orange"),
#         "B": Vehicle("B", "horizontal", "green"),
#         "C": Vehicle("C", "horizontal", "blue"),
#         "D": Vehicle("D", "vertical", "cyan"),
#         "E": Vehicle("E", "horizontal", "orange"),
#         "F": Vehicle("F", "horizontal", "green"),
#         "G": Vehicle("G", "vertical", "cyan"),
#         "H": Vehicle("H", "horizontal", "orange"),
#         "I": Vehicle("I", "horizontal", "green"),
#         "J": Vehicle("J", "vertical", "yellow"),
#         "K": Vehicle("K", "horizontal", "blue"),
#         "L": Vehicle("L", "horizontal", "orange"),
#         "R": Vehicle("R", "horizontal", "red")
#         }

def field3():
    tiles = "0AABBB0CCDEERRFD0IGGFHHIJ0K0LLJ0K000"
#    0AABBB
#    0CCDEE
#    RRFD0I
#    GGFHHI
#    J0K0LL
#    J0K000

    vehicles = {
        "A": 2,
        "B": 3,
        "C": 2,
        "D": 2,
        "E": 2,
        "F": 2,
        "G": 2,
        "H": 2,
        "I": 2,
        "J": 2,
        "K": 2,
        "L": 2,
        "R": 2
    }
    

    field = Field(tiles, 6, set(["A","B","C","E","G","H","L","R"]), set(["D","F","I","J","K"]), vehicles)
    return field
    
# def vehicles3():
#     return {
#         "A": Vehicle("A", "horizontal", "blue"),
#         "B": Vehicle("B", "horizontal", "yellow"),
#         "C": Vehicle("C", "horizontal", "orange"),
#         "D": Vehicle("D", "vertical", "blue"), 
#         "E": Vehicle("E", "horizontal", "green"),
#         "F": Vehicle("F", "vertical", "cyan"), 
#         "G": Vehicle("G", "horizontal", "green"), 
#         "H": Vehicle("H", "horizontal", "blue"),
#         "I": Vehicle("I", "vertical", "cyan"), 
#         "J": Vehicle("J", "vertical", "orange"),
#         "K": Vehicle("K", "vertical", "green"),
#         "L": Vehicle("L", "horizontal", "green"),
#         "R": Vehicle("R", "horizontal", "red")
#     }
    
def field4():
    tiles = "ABBB0U000A00C0UVVV000C0U00TDD0C0SSSTERRF0000TE0GF0QQQPHHGKLL00PI0GKM000PIJJJMNNOO"
    
   # ABBB0U000
   # A00C0UVVV
   # 000C0U00T
   # DD0C0SSST
   # ERRF0000T
   # E0GF0QQQP
   # HHGKLL00P
   # I0GKM000P
   # IJJJMNNOO

    vehicles = {
        "A": 2,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 2,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 2,
        "J": 3,
        "K": 2,
        "L": 2,
        "M": 2,
        "N": 2,
        "O": 2,
        "P": 3,
        "Q": 3,
        "S": 3,
        "T": 3,
        "U": 3,
        "V": 3,
        "R": 2
    }

    field = Field(tiles, 9, set(["B", "D", "H", "J", "L", "N", "O", "Q", "S", "V", "R"]), set(["A", "C", "E", "F", "G", "I", "K", "M", "P", "T", "U"]), vehicles)
    return field
    
# def vehicles4():
#     return {
#         "A": Vehicle("A", "vertical", "green"),
#         "B": Vehicle("B", "horizontal", "yellow"),
#         "C": Vehicle("C", "vertical", "purple"),
#         "D": Vehicle("D", "horizontal", "blue"), 
#         "E": Vehicle("E", "vertical", "cyan"), 
#         "F": Vehicle("F", "vertical", "green"),
#         "G": Vehicle("G", "vertical", "yellow"), 
#         "H": Vehicle("H", "horizontal", "orange"),
#         "I": Vehicle("I", "vertical", "blue"),
#         "J": Vehicle("J", "horizontal", "grey"),
#         "K": Vehicle("K", "vertical", "blue"),
#         "L": Vehicle("L", "horizontal", "green"),
#         "M": Vehicle("M", "vertical", "orange"),
#         "N": Vehicle("N", "horizontal", "cyan"),
#         "O": Vehicle("O", "horizontal", "green"), 
#         "P": Vehicle("P", "vertical", "pink"),
#         "Q": Vehicle("Q", "horizontal", "purple"),
#         "S": Vehicle("S", "horizontal", "pink"), 
#         "T": Vehicle("T", "vertical", "yellow"),
#         "U": Vehicle("U", "vertical", "grey"), 
#         "V": Vehicle("V", "horizontal", "purple"),
#         "R": Vehicle("R", "horizontal", "red")
#     }
    
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

    vehicles = {
        "A": 3,
        "B": 3,
        "C": 2,
        "D": 2,
        "E": 2,
        "F": 3,
        "G": 2,
        "H": 2,
        "I": 2,
        "J": 2,
        "K": 2,
        "L": 3,
        "M": 2,
        "N": 3,
        "O": 2,
        "P": 3,
        "Q": 2,
        "S": 2,
        "T": 2,
        "U": 2,
        "V": 2,
        "W": 2,
        "X": 2,
        "R": 2
    }

    field = Field(tiles, 9, set(["A","F","H","I","K","L","O","Q","T","U","X","R"]), set(["B","C","D","E","G","J","M","N","P","S","V","W"]), vehicles)
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

    vehicles = {
        "A": 2,
        "B": 2,
        "C": 2,
        "D": 3,
        "E": 2,
        "F": 3,
        "G": 2,
        "H": 3,
        "I": 2,
        "J": 2,
        "K": 2,
        "L": 3,
        "M": 2,
        "N": 2,
        "O": 2,
        "P": 3,
        "Q": 2,
        "S": 2,
        "T": 2,
        "U": 3,
        "V": 2,
        "W": 3,
        "X": 3,
        "Y": 2,
        "Z": 2,
        "R": 2
    }

    field = Field(tiles, 9, set(["A","B","D","E","H","I","J","O","Q","T","U","V","X","Y","R"]), set(["C","F","G","K","L","M","N","P","S","W","Z"]), vehicles)
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
  
def field7():
    tiles = "A00000XUUUVVA0000TX000(-BBBCCTYWW0(-DE000SY^^&&0DEFFFSY%%%00DERRQZ000000GGGOQZ170899HHHOPP1708!!IIJNNN16660$00JMMM2055@$0000002004@#0KKLLL2334@#"
    
    #A00000XUUUVV
    #A0000TX000(-
    #BBBCCTYWW0(-
    #DE000SY^^&&0
    #DEFFFSY%%%00
    #DERRQZ000000
    #GGGOQZ170899
    #HHHOPP1708!!
    #IIJNNN16660$
    #00JMMM2055@$
    #0000002004@#
    #0KKLLL2334@#
    vehicles = {
        "A": 2,
        "B": 3,
        "C": 2,
        "D": 3,
        "E": 3,
        "F": 3,
        "G": 3,
        "H": 3,
        "I": 2,
        "J": 2,
        "K": 2,
        "L": 3,
        "M": 3,
        "N": 3,
        "O": 2,
        "P": 2,
        "Q": 2,
        "S": 2,
        "T": 2,
        "U": 3,
        "V": 2,
        "W": 2,
        "X": 2,
        "Y": 3,
        "Z": 2,
        "1": 3,
        "2": 3,
        "3": 2,
        "4": 2,
        "5": 2,
        "6": 3,
        "7": 2,
        "8": 2,
        "9": 2,
        "!": 2,
        "@": 3,
        "#": 2,
        "$": 2,
        "%": 3,
        "^": 2,
        "&": 2,
        "(": 2, 
        "-": 2, 
        "R": 2,
    }

    field = Field(tiles, 12, set(["B","C","F","G","H","I","K","L","M","N","P","U","V","W","3","5","6","9","!","%","^","&","R"]),\
    set(["A","D","E","J","O","Q","S","T","X","Y","Z","1","2","4","7","8","@","#","$","(","-"]), vehicles)
    return field


def vehicles7():
    return{
        "A": Vehicle("A", "vertical", "green"),
        "B": Vehicle("B", "horizontal", "yellow"),
        "C": Vehicle("C", "horizontal", "oranje"),
        "D": Vehicle("D", "vertical", "purple"), 
        "E": Vehicle("E", "vertical", "pink"), 
        "F": Vehicle("F", "horizontal", "grey"),
        "G": Vehicle("G", "horizontal", "grey"), 
        "H": Vehicle("H", "horizontal", "yellow"),
        "I": Vehicle("I", "horizontal", "orange"),
        "J": Vehicle("J", "vertical", "green"),
        "K": Vehicle("K", "horizontal", "green"),
        "L": Vehicle("L", "horizontal", "yellow"),
        "M": Vehicle("M", "horizontal", "yellow"),
        "N": Vehicle("N", "horizontal", "purple"),
        "O": Vehicle("O", "vertical", "cyan"), 
        "P": Vehicle("P", "horizontal", "green"),
        "Q": Vehicle("Q", "vertical", "orange"),
        "S": Vehicle("S", "vertical", "green"), 
        "T": Vehicle("T", "vertical", "cyan"),
        "U": Vehicle("U", "horizontal", "purple"), 
        "V": Vehicle("V", "horizontal", "cyan"),
        "W": Vehicle("W", "horizontal", "green"),
        "X": Vehicle("X", "vertical", "blue"),
        "Y": Vehicle("Y", "vertical", "yellow"),
        "Z": Vehicle("Z", "vertical", "cyan"), 
        "1": Vehicle("1", "vertical", "yellow"),
        "2": Vehicle("2", "vertical", "grey"),
        "3": Vehicle("3", "horizontal", "blue"),
        "4": Vehicle("4", "vertical", "cyan"), 
        "5": Vehicle("5", "horizontal", "green"), 
        "6": Vehicle("6", "horizontal", "yellow"),
        "7": Vehicle("7", "vertical", "blue"), 
        "8": Vehicle("8", "vertical", "cyan"),
        "9": Vehicle("9", "horizontal", "green"),
        "!": Vehicle("!", "horizontal", "blue"),
        "@": Vehicle("@", "vertical", "purple"),
        "#": Vehicle("#", "vertical", "cyan"),
        "$": Vehicle("$", "vertical", "green"),
        "%": Vehicle("%", "horizontal", "purple"),
        "^": Vehicle("^", "horizontal", "orange"), 
        "&": Vehicle("&", "horizontal", "cyan"),
        "(": Vehicle("(", "vertical", "orange"), 
        "-": Vehicle("-", "vertical", "blue"), 
        "R": Vehicle("R", "horizontal", "red")
    }
  









    





















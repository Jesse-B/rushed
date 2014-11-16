import copy
import games
import Queue

from field import Field, Vehicle


def BFSearch(fieldsQueue, visited):
    solution = None
    while solution is None:
        field = fieldsQueue.get()
        for x in range(len(field.vehicles)):
            vehicle = field.vehicles[x]
            moves = vehicle.getPossibleMoves(field)
            for move in moves:
                copyField = copy.deepcopy(field)
                copyVehicle = copyField.vehicles[x]
                copyVehicle.move(copyField, move[0], move[1], move[2])
                if not copyField in visited:
                    visited.add(copyField)
                    fieldsQueue.put(copyField)
                if copyVehicle.color == "red":
                    if copyVehicle.positions[-1] == copyField.exit:
                        print "FOUND SOLUTION"
                        print copyField
                        solution = copyField
    return solution

if __name__ == "__main__":
    field = games.field2()
    queue = Queue.Queue()
    queue.put(field)
    BFSearch(queue, set([field]))

from enum import Enum

class ValidCommands(Enum):
    """ Representa os comandos válidos para o parser de comandos """
    
    PLACE = "PLACE"
    MOVE = "MOVE"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"
    REPORT = "REPORT"


class DataCommand(object):

    def __init__(self, angle, direction=None):
        self.angle = angle
        self.direction = direction

    def __add__(self, other):
        self.angle += other.angle
        if self.angle % 360 > 0 and self.angle // 360:
            self.angle = self.angle - 360

        if Directions.RIGHT == other.direction:
                list_directions = [d for d in Directions if d.value[1] == self.angle and d.value[0] != ValidCommands.RIGHT]
                if len(list_directions) == 1:
                    self.direction = list_directions[0]
                    return self

        if Directions.LEFT == other.direction:
                list_directions = [d for d in Directions if d.value[1] == self.angle and d.value[0] != ValidCommands.LEFT]
                if len(list_directions) == 1:
                    self.direction = list_directions[0]
                    return self

        
        direction_found = [d for d in Directions if d.value[1] == self.angle]
        if len(direction_found) == 1:
            self.direction =  direction_found[0]
            return self

        return self


class Directions(Enum):
    """ Representa as direções que é representado por um comando e um angulo """    
    def __init__(self, direction, angle):
        self.direction = direction
        self.angle = angle

    NORTH = ValidCommands.NORTH, 90
    SOUTH = ValidCommands.SOUTH, 270
    EAST = ValidCommands.EAST, 180
    WEST = ValidCommands.WEST, 360
    RIGHT = ValidCommands.RIGHT, +90
    LEFT = ValidCommands.LEFT, -90

class Side:

    RIGHT = Directions.RIGHT
    LEFT = Directions.LEFT


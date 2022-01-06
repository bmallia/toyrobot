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


class Directions(Enum):
    """ Representa as direções que é representado por um comando e um angulo """
    def __init__(self, command, angle, valid_direction):
        self.command = command
        self.angle = angle
        self.valid_direction = valid_direction

    NORTH = ValidCommands.NORTH, 90, True
    SOUTH = ValidCommands.SOUTH, 270, True
    EAST = ValidCommands.EAST, 180, True
    WEST = ValidCommands.WEST, 0, True
    RIGHT = ValidCommands.RIGHT, +90, False
    LEFT = ValidCommands.LEFT, -90, False

    def __add__(self, other):
        self.angle += other.angle

        direction_found = [d for d in Directions if d.value[1] == self.angle and d.value[2] == True]
        
        if len(direction_found) == 1:
            return direction_found[0]
        
        return None
        


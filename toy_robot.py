"""
The definition of the ToyRobot
"""

TABLE_WIDTH = 5
TABLE_HEIGHT = 5
DIRECTIONS_IN_ORDER = ["NORTH", "EAST", "SOUTH", "WEST"]  # clockwise
DIRECTIONS = {"NORTH": (0, 1),
              "SOUTH": (0, -1),
              "EAST": (1, 0),
              "WEST": (-1, 0)}

class ToyRobot():
    def __init__(self):
        self.__xPos = None
        self.__yPos = None
        self.__facing = None
        self.__placed = False

    @staticmethod
    def __is_on_table(x, y):
        if x < 0 or x >= TABLE_WIDTH or y < 0 or y >= TABLE_HEIGHT:
            return False
        return True

    def place(self, x, y, facing):
        # print(x,y,facing)
        # check the input parameters are valid
        if not self.__is_on_table(x, y):
            return "The initial position is invalid, should between (0,0) and (4,4)."

        if facing not in DIRECTIONS_IN_ORDER:
            return "Unknown facing direction, possible values: NORTH, SOUTH, EAST, WEST(case insensitive)."

        # update toy robot's properties
        self.__xPos = x
        self.__yPos = y
        self.__facing = facing
        self.__placed = True

        return "Placed."

    def move(self):
        # if the robot has not been placed, no other command can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        # get the new position with one step movement
        x_move = self.__xPos + DIRECTIONS[self.__facing][0]
        y_move = self.__yPos + DIRECTIONS[self.__facing][1]

        # check whether the robot will fall off with the movement
        if not self.__is_on_table(x_move, y_move):
            return "Can\'t move, toy robot will fall off the table."

        # the command can be executed, update toy robot's position
        self.__xPos = x_move
        self.__yPos = y_move
        return "Moved."

    def right(self):
        # if the robot has not been placed, no other command can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        self.__facing = DIRECTIONS_IN_ORDER[(DIRECTIONS_IN_ORDER.index(self.__facing) + 1) % len(DIRECTIONS_IN_ORDER)]
        return "Turned Right."

    def left(self):
        # if the robot has not been placed, no other command can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        self.__facing = DIRECTIONS_IN_ORDER[(DIRECTIONS_IN_ORDER.index(self.__facing) - 1 + 4) % len(DIRECTIONS_IN_ORDER)]
        return "Turned Left."

    def report(self):
        # if the robot has not been placed, no other command can be executed except PLACE
        if not self.__placed:
            return "Toy robot has not been placed on the table."

        report_info = "X: {0}, Y: {1}, FACING: {2}.".format(self.__xPos, self.__yPos, self.__facing)
        return report_info



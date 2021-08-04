"""
All the excuting result from the user interface
"""

SUCCESS_PLACE = "Placed.\n"
SUCCESS_MOVE = "Moved.\n"
SUCCESS_LEFT = "Turned Left.\n"
SUCCESS_RIGHT = "Turned Right.\n"
REPORT_FORMAT = "X: {0}, Y: {1}, FACING: {2}.\n"

FAIL_UNKNOWN_COMMAND = "Unknown command.\n"
FAIL_INVALID_ARGUMENTS = "Invalid arguments.\n"
FAIL_INVALID_POSITION = "The initial position is invalid, should between (0,0) and (4,4).\n"
FAIL_INVALID_FACING = "Unknown facing direction, possible values: NORTH, SOUTH, EAST, WEST(case insensitive).\n"
FAIL_NOT_PLACED = "Toy robot has not been placed on the table.\n"
FAIL_FALL_OFF = "Can\'t move, toy robot will fall off the table.\n"

"""
Test Command.
"""

import unittest

from cmd import proc_cmd
from toy_robot import ToyRobot
from tests.stub import *
from tests.results import *


class CommandUnitTest(unittest.TestCase):

    def test_unsupported_command(self):
        robot = ToyRobot()

        command = "RANDOMCOMMAND"
        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_UNKNOWN_COMMAND))

    # MOVE/LEFT/RIGHT/REPORT commands, no argument required
    # Test these commands with extra arguments
    def test_command_extra_arguments(self):
        robot = ToyRobot()

        command = "MOVE 1\n" \
                  + "LEFT 90\n" \
                  + "RIGHT 90\n" \
                  + "REPORT OK\n"

        stub_stdin(self, command)

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

    # Test PLACE command with valid and invalid arguments
    # Format: PLACE x, y, facing.
    # 3 arguments required, spaces between arguments can be handled flexibly
    # The values of x and y are in the range of [0,4]
    # the value of facing can be "NORTH", "SOUTH", "EAST", "WEST", case insensitive.
    def test_command_place_arguments(self):
        robot = ToyRobot()

        command = "PLACE 0, 4, NORTH\n" \
                  + "PLACE 0, 4, south\n" \
                  + "PLACE 0, 4\n" \
                  + "PLACE 0, NORTH\n" \
                  + "PLACE NORTH\n" \
                  + "PLACE 0, 0, NORTH, EAST\n" \
                  + "PLACE\n" \
                  + "PLACE 5, 1, NORTH\n" \
                  + "PLACE 1, 5, NORTH\n" \
                  + "PLACE 1, 4, MIDDLE\n" \
                  + "PLACE 0, 0, EAST\n" \
                  + "PLACE 4, 4, WEST\n" \
                  + "PLACE 4 4 WEST\n" \
                  + "PLACE 2,  3,WEST\n"

        stub_stdin(self, command)

        # normal: "PLACE 0, 4, NORTH\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # lowercase facing: "PLACE 0, 4, south\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # missing facing: "PLACE 0, 4\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # missing x or y: "PLACE 0, NORTH\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # missing x and y: "PLACE NORTH\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # extra arguments: "PLACE 0, 0, NORTH, EAST\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # no argument: "PLACE\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # x out of range: "PLACE 5, 1, NORTH\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_POSITION))

        # y out of range: "PLACE 1, 5, NORTH\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_POSITION))

        # unsupported facing: "PLACE 1, 4, MIDDLE\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_FACING))

        # boundary x and y: "PLACE 0, 0, EAST\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # boundary x and y: "PLACE 4, 4, WEST\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # no comma between arguments: "PLACE 4 4 WEST\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_INVALID_ARGUMENTS))

        # no space or extra space between arguments: "PLACE 2,  3,WEST\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))


    # all commands are case insensitive
    def test_command_lowercase_command(self):
        robot = ToyRobot()

        command = "place 2, 2, north\n" \
                  + "move\n" \
                  + "left\n" \
                  + "right\n" \
                  + "report\n" \
                  + "PLACE 2,2,north\n" \
                  + "MOVE\n" \
                  + "LEFT\n" \
                  + "RIGHT\n" \
                  + "REPORT\n"

        stub_stdin(self, command)

        # lower case PLACE: "place 2, 2, north\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # lower case MOVE: "move\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_MOVE))

        # lower case LEFT: "left\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_LEFT))

        # lower case RIGHT: "right\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_RIGHT))

        # lower case report: "report\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), REPORT_FORMAT.format(2, 3, "NORTH")))

        # upper case PLACE: "PLACE 2, 2, north\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_PLACE))

        # upper case MOVE: "MOVE\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_MOVE))

        # upper case LEFT: "LEFT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_LEFT))

        # upper case RIGHT: "RIGHT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), SUCCESS_RIGHT))

        # upper case report: "REPORT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), REPORT_FORMAT.format(2, 3, "NORTH")))

    # discard all commands in the sequence until a valid PLACE command has been executed.
    def test_command_order(self):
        robot = ToyRobot()

        command = "MOVE\n" \
                  + "LEFT\n" \
                  + "RIGHT\n" \
                  + "REPORT\n"

        stub_stdin(self, command)

        # "MOVE\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_NOT_PLACED))

        # "LEFT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_NOT_PLACED))

        # "RIGHT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_NOT_PLACED))

        # "REPORT\n"
        stub_stdout(self)
        proc_cmd(robot)
        self.assertEqual(str(sys.stdout.getvalue(), FAIL_NOT_PLACED))


if __name__ == '__main__':
    unittest.main()
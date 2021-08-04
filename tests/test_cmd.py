"""
Test Command.
"""

import unittest

class CommandUnitTest(unittest.TestCase):

    def test_unsupported_command(self):
        pass

    # MOVE/LEFT/RIGHT/REPORT commands, no argument required
    # Test these commands with extra arguments
    def test_command_extra_arguments(self):
        pass

    # Test PLACE command:
    # Format: PLACE x, y, facing.
    # Test PLACE command with valid and invalid arguments
    def test_command_place_arguments(self):
        pass

    # all commands are case insensitive
    def test_command_lowercase_command(self):
        pass

    # discard all commands in the sequence until a valid PLACE command has been executed.
    def test_command_order(self):
        pass


if __name__ == '__main__':
    unittest.main()
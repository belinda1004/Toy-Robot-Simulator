"""
Check and execute commands
"""

def proc_cmd():
    command_str = input("Command: ").upper()
    command_list = command_str.split(" ")
    command = command_str[0]

    if not command in ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]:
        print("Unknown Command.")
        return

    if (command != "PLACE" and len(command_list) > 1) or \
        (command == "PLACE" and len(command_list) != 4):
        print("Invalid arguments.")
        return

    if command == "PLACE":
        pass
    elif command == "MOVE":
        pass
    elif command == "LEFT":
        pass
    elif command == "RIGHT":
        pass
    elif command == "REPORT":
        pass
    return



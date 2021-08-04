"""
Check and execute commands
"""

def proc_cmd(robot):
    command_str = input("Command: ").upper()
    command_list = command_str.split(" ")
    command = command_list[0]
    # print(command, command_list)
    if not command in ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]:
        print("Unknown command.")
        return

    if (command != "PLACE" and len(command_list) > 1) or \
        (command == "PLACE" and len(command_list) < 2):
        print("Invalid arguments.")
        return

    if command == "PLACE":
        try:
            x, y, facing = "".join(command_list[1:]).split(",")
            x = int(x)
            y = int(y)
        except ValueError:
            print("Invalid arguments.")
            return
        info = robot.place(x, y, facing)
    elif command == "MOVE":
        info = robot.move()
    elif command == "LEFT":
        info = robot.left()
    elif command == "RIGHT":
        info = robot.right()
    elif command == "REPORT":
        info = robot.report()

    print(info)
    return



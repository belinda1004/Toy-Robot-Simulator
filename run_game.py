from cmd import proc_cmd
from toy_robot import ToyRobot

def run_game():
    print("Game Start...")
    while True:
        proc_cmd()


if __name__ == '__main__':
    run_game()
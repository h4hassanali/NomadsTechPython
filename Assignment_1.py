import argparse
from time import sleep
import keyboard

def on_space_press(event, space_button_state):
    """This function updates the state to True when Space key is pressed"""
    space_button_state[0] = True

def run_counter(num_sec):
    space_button_state = [False]
    keyboard.on_press_key('space', lambda event: on_space_press(event, space_button_state))
    for i in range(num_sec):
        if space_button_state[0]:
            break
        print(i)
        sleep(1)

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('--target', type=int, required=True)
        args = parser.parse_args()
        if args.target <= 0:
            raise ValueError("The --target value must be a positive integer.")
        run_counter(args.target)


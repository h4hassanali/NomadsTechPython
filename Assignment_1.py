import argparse
from time import sleep
import keyboard

class SpaceButtonHandler:
    """Class for space button handeling"""
    def __init__(self):
        self.space_pressed = False

    def on_space_press(self, event):
        """Sets space_pressed to True when Space key is pressed"""
        self.space_pressed = True

def run_counter(num_sec):
    handler = SpaceButtonHandler()
    keyboard.on_press_key('space', handler.on_space_press)
    for i in range(num_sec):
        if handler.space_pressed:
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

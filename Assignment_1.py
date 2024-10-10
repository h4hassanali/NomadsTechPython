from sys import argv
from time import sleep
import keyboard

def on_space_press(event):
    """ this function is callback function, which turns
    space button to 'True' when Space key is pressed """
    global space_button
    space_button = True

def run_counter(num_sec):
    keyboard.on_press_key('space', on_space_press)
    for i in range(num_sec):
        if space_button:
            break
        print(i)
        sleep(1)

space_button = False
seconds = int(argv[1])
run_counter(seconds)

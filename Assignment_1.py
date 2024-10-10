from sys import argv
from time import sleep
import keyboard

def on_space_press(event, state):
    """ this function is callback function, which updates 
    the state to True when Space key is pressed """
    state['space_button'] = True

def run_counter(num_sec):
    space_button_state = {'space_button': False}
    keyboard.on_press_key('space', lambda event: on_space_press(event, space_button_state))
    
    for i in range(num_sec):
        if space_button_state['space_button']:
            break
        print(i)
        sleep(1)

seconds = int(argv[1])
run_counter(seconds)

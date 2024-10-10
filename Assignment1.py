# Task 1 : Python Programming
#  Create a python commandline app:
# - which accepts inputs as commandline arguments
# - displays a counter which increments every second, 
#   till it reaches the input number
# - The counter stops if it is interrupted when space key 
#   is pressed
# - Upload in a git repo. The main branch should have only
#   a README.md file. The code should be in a branch called 
#   code. Create a PR into main branch from code branch.

# Concepts I have used :
# 1. Argument Parsing
# 2. Time Module
# 3. Keyboard input handeling
# 4. Callback functions
# 5. Version Control using git


from sys import argv
from time import sleep
import keyboard

def on_space_press(event):
    """ this function is callback function, which turns
    space button to 'True' when Space key is pressed """
    global space_button
    space_button = True

def num_generator(num_sec):
    """ I have used generator because of its memory efficiency,
    As generator doesnt store all values once in memory , hence 
    for the case of large number of data it will help us out"""
    for number in range(num_sec):
        yield number # yield pause the execution..

def run_counter(num_sec):
    """ This function run the counter app, it first generate
    a number, then a event lister is added in which two arguments
    are passed , one is the key from keyboard and other is the
    callback function , on_press_key is higher order function,
    In loop we generate next number while continuously checking
    for the value of space_button. """
    num = num_generator(num_sec)
    keyboard.on_press_key('space', on_space_press)
    for i in range(num_sec):
        if space_button:
            break
        print(next(num))
        sleep(1)

space_button = False
seconds = int(argv[1])
run_counter(seconds)





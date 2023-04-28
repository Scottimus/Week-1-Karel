from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #make karel build column
    build_column()
    next_column()
    build_column()
    next_column()
    build_column()
    next_column()
    build_column()
    turn_left()
    
def build_column():
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_around()
    move()
    move()
    move()
    move()
    
def turn_around():
    turn_left()
    turn_left()
    
def next_column():
    face_forward()
    for i in range(4):
        move()
    
def face_forward():
    turn_left()

if __name__ == '__main__':
    main()

#second test 3
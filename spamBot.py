from pynput.keyboard import Key, Controller
from pynput import keyboard
from time import sleep
board = Controller()
def spam(x):
    for i in range(x):
        board.type('fish\n')
        #board.press(Key.enter)
def doSpam(key):
    if key==Key.down:
        listener.stop()
    elif key==Key.up:
        spam(50)
listener = keyboard.Listener(on_press=doSpam)
listener.start()

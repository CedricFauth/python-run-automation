from pynput import keyboard
import time
import sys
import os

def on_activate():
    print("Running command: ")
    time.sleep(0.5)
    os.system(command)

def exit():
    sys.exit()

def main():
    
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], '"COMMAND"')
        sys.exit()
    global command
    command = sys.argv[1]
    with keyboard.GlobalHotKeys({
        '<ctrl>+s': on_activate,
        '<esc>': exit}) as h:
        h.join()


if __name__ == "__main__":
    main()


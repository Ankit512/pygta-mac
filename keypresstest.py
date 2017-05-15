from pynput import keyboard
import threading

keys = []

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if (key.char.upper() not in keys):
            keys.append(key.char.upper())
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        print('{0} released'.format(
            key))
        keys.remove(key.char.upper())
    except AttributeError:
        print('special key released')

def listen_keys():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

t = threading.Thread(target=listen_keys)
t.daemon = True
t.start()

def key_check():
    return keys

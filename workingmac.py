import pydirectinput
from getfiledict import getmaclist
import time
from pynput.keyboard import KeyCode
from functools import partial

pydirectinput.PAUSE = 0
pydirectinput.MINIMUM_SLEEP = 0
pydirectinput.MINIMUM_DURATION = 0

script_name = getmaclist()



def launchmac(key):
    for key_name,event_list in script_name.items():
        if key_name == key:
            for event in event_list:
                if event.startswith("bindedkey="):
                    pass
                else:
                    if event.replace('.', '', 1).isdigit():
                        time.sleep(float(event))
                    else:
                        new_event = event.split(" ")
                        if len(new_event[1]) == 4:
                            pydirectinput.keyDown(new_event[0])
                        else:
                            pydirectinput.keyUp(new_event[0])

## populated combination ##


def getmachotkeys():
    global combination_to_function
    combination_to_function = {}
    for key,value in script_name.items():
        if value[0].startswith("bindedkey="):
            code = int(value[0][10:])
            combination_to_function[frozenset([KeyCode(code)])] = (partial(launchmac, key))
    return combination_to_function



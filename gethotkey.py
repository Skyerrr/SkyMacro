from pynput.keyboard import Listener
import time
from threading import Thread


def get_hotkey():
    inputs = []
    def on_press(key):
        vk = key.vk if hasattr(key, 'vk') else key.value.vk
        inputs.append(key)
        inputs.append(vk)


    with Listener(on_press=on_press) as ls:
        def time_out(period_sec: int):
            time.sleep(period_sec)  # Listen to keyboard for period_sec seconds
            ls.stop()

        Thread(target=time_out, args=(3.0,)).start()
        ls.join()
        return inputs




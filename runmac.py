from workingmac import getmachotkeys
from pynput import keyboard


# Create a mapping of keys to function (use frozenset as sets/lists are not hashable - so they can't be used as keys)

combination_to_function = getmachotkeys()
# The currently pressed keys (initially empty)
pressed_vks = set()

class Run_all():
    def __init__(self):
        super(Run_all, self).__init__()
    def run_mac(self, loop):
        self.pressed_loop = loop
        global listener
        listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        listener.start()

    def get_vk(self, key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, 'vk') else key.value.vk


    def is_combination_pressed(self, combination):
        """ Check if a combination is satisfied using the keys pressed in pressed_vks """
        return all([self.get_vk(key) in pressed_vks for key in combination])
    def on_press(self, key):
        """ When a key is pressed """
        vk = self.get_vk(key)  # Get the key's vk
        pressed_vks.add(vk)  # Add it to the set of currently pressed keys
        if self.pressed_loop:
            for combination in combination_to_function:  # Loop through each combination
                if self.is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                    combination_to_function[combination]() # If so, execute the function


        elif not self.pressed_loop:
            for combination in combination_to_function:  # Loop through each combination
                if self.is_combination_pressed(combination):  # Check if all keys in the combination are pressed
                    combination_to_function[combination]()  # If so, execute the function

            try:
                vk = self.get_vk(key)  # Get the key's vk
                pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys

            except KeyError:
                pass

    def on_release(self, key):
        """ When a key is released """
        try:
            vk = self.get_vk(key)  # Get the key's vk
            pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys
        except KeyError:
            pass


    def stop_mac(self):
        listener.stop()
























































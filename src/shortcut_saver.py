from pynput import keyboard

from config_handler import Config_handler

class Shortcut_saver:

    def __init__(self):
        self.pressed = set()

    def _on_press(self, key):
        self.pressed.add(key)

    def _on_release(self, key):
        self.pressed.remove(key)

    def save_config(self):
        data = {
            "shortcut_keys" : [
                str(self.listener.canonical(key)) for key in self.pressed
            ]
        }
        Config_handler.set_shortcuts(data)

    def listen(self):
        listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release)
        listener.start()

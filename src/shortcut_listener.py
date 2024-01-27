import json
from .exceptions import CorruptedConfigFileError
from pynput import keyboard

class Keyboard_listener:


    def __init__(self):
        self.shortcuts = set()
        self.pressed = set()
        self._unpack_config()


    def _unpack_config(self):
        try:
            with open("config.json", "r") as json_file:
                json_data = json.load(json_file)
                
                if not "shortcut_keys" in json_data.keys():
                    raise CorruptedConfigFileError("Config file incorrectly formatted")
                
                self.shortcuts = set(json_data["shortcut_keys"])
        except FileNotFoundError:
            raise CorruptedConfigFileError("Config file does not exist or exists in incorrect place")


    def _on_click(self, key):
        self.pressed.add(key)
        if self.shortcuts.issubset(self.pressed):
            return False #break listener

    def _on_release(self, key):
        self.pressed.remove(key)

    def _clear(self):
        self.pressed.clear()

    def listen(self):
        self._clear() 
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as listener:
            listener.join()

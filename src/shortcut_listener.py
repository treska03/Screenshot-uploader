import json
from exceptions import CorruptedConfigFileError
from pynput import keyboard

class Keyboard_listener:

    def __init__(self):
        self._shortcuts = set()
        self._unpack_config()

    def _unpack_config(self):
        try:
            with open("config.json", "r") as json_file:
                json_data = json.load(json_file)
                
                if not "shortcut_keys" in json_data.keys():
                    raise CorruptedConfigFileError("Config file incorrectly formatted")
                
                self._shortcuts = set(json_data["shortcut_keys"])
        except FileNotFoundError:
            raise CorruptedConfigFileError("Config file does not exist or exists in incorrect place")


    def _on_hotkey_activate(self):
        self.l.stop()

    def _for_canonical(self, f):
        return lambda k: f(str(self.l.canonical(k)))

    def listen(self):
        hotkey = keyboard.HotKey(
            self._shortcuts, self._on_hotkey_activate
        )
        with keyboard.Listener(
                on_press=self._for_canonical(hotkey.press),
                on_release=self._for_canonical(hotkey.release)) as self.l:
            self.l.join()

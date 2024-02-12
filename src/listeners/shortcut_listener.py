from util.config_handler import Config_handler
from pynput import keyboard

class Keyboard_listener:

    def __init__(self):
        self._shortcuts = Config_handler.get_shortcuts()

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

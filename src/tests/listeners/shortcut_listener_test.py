import unittest
from src.main.listeners.shortcut_listener import Keyboard_listener

listener = Keyboard_listener()

class TestListener(unittest.TestCase):

    def test_unpacking(self):
        self.assertEqual(set(["Key.alt", "Key.shift", "Key.cmd"]), listener._shortcuts)



if __name__ == "__main__":
    unittest.main()
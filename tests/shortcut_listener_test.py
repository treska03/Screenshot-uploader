import unittest
from src.listeners.shortcut_listener import Keyboard_listener

listener = Keyboard_listener()

class TestListener(unittest.TestCase):

    def test_unpacking(self):
        self.assertEqual(set(["shift", "alt_l", "cmd"]), listener.shortcuts)



if __name__ == "__main__":
    unittest.main()
import unittest
from src.main.util.screenshoter import Screenshooter as ss

class TestScreenshoter(unittest.TestCase):

    def test_normal_bbox(self):
        ss.take_screenshot(100, 200, 300, 400)
        ss.take_screenshot(250, 0, 350, 4)
        ss.take_screenshot(0, 0, 1, 1)

    def test_weird_bbox(self):
        ss.take_screenshot(500, 100, 100, 500)
        ss.take_screenshot(200, 200, 10, 10)
    
    def test_should_break_bbox(self):
        self.assertRaises(ValueError, ss.take_screenshot, 100, 0, 0, 0)
        self.assertRaises(ValueError, ss.take_screenshot, 2, 2, 2, 2)
    

if __name__ == "__main__":
    unittest.main()

import unittest
from src.main.util.imgur import API_Handler
from src.main.util.exceptions import InvalidScreenshotException
from src.main.util.config_handler import Config_handler

CLIENT_ID = Config_handler.get_token()

handler = API_Handler(CLIENT_ID)

class TestImgur(unittest.TestCase):
    
    def test_correct_screenshot(self):
        with open("tests/samples/ss1.png", "rb") as screenshot:
            InvalidScreenshotException, handler.upload(screenshot)


    def test_incorrect_screenshot(self):
        self.assertRaises(InvalidScreenshotException, handler.upload, "not a file")
        
        with open(".gitignore", "rb") as not_screenshot:
            self.assertRaises(InvalidScreenshotException, handler.upload, not_screenshot)


    def test_incorrect_screenshot_opener(self):
        with open("tests/samples/ss1.png", "r") as screenshot:
            self.assertRaises(UnicodeDecodeError, handler.upload, screenshot)
            

if __name__ == "__main__":
    unittest.main()
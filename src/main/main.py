import json
from src.main.util.config_handler import Config_handler
from src.main.util.imgur import API_Handler
from src.main.listeners.mouse_listener import Mouse_listener
from src.main.listeners.shortcut_listener import Keyboard_listener
from src.main.util.notifications import Notification
from src.main.util.screenshoter import Screenshooter as ss
from src.main.util.clipboard import Clipboard

class Main:

    @staticmethod
    def main_loop():
        TOKEN = Config_handler.get_token()
        handler = API_Handler(TOKEN)
        listener = Keyboard_listener()
        mouse_listener = Mouse_listener()

        while True:
            listener.await_hotkey()
            Notification.notify(title="Screenshot!", message="Take screenshot", 
                                app_name="Screener", timeout=5)
            x1, y1, x2, y2 = mouse_listener.select_area()
            screenshot = ss.take_screenshot(x1, y1, x2, y2)

            
            byte_screenshot = ss.screenshot_as_bytes(screenshot)
            response = handler.upload(byte_screenshot)
            response_dict = json.loads(response.decode("utf-8"))

            Clipboard.string_to_clipboard(response_dict["data"]["link"])
            
            Notification.notify(
                title="Screenshot taken!", 
                message="Link to screenshot has been coppied to your clipboard",
                app_name="Screener",
                timeout=5
            )


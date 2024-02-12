import pyscreenshot as ImageGrab
import io

class Screenshooter:

    @staticmethod
    def take_screenshot(x_start, y_start, x_end, y_end):
        x_start, x_end = min(x_start, x_end), max(x_start, x_end)
        y_start, y_end = min(y_start, y_end), max(y_start, y_end)
        return ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))
    
    @staticmethod
    def screenshot_as_bytes(screenshot):
        output = io.BytesIO()
        screenshot.save(output, format='JPEG')
        return output.getvalue()
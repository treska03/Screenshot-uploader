from io import BytesIO
import win32clipboard


class Clipboard:

    @staticmethod
    def image_to_clipboard(image):
        output = BytesIO()
        image.convert('RGB').save(output, 'DIB')
        data = output.getvalue()
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

    @staticmethod
    def string_to_clipboard(s):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(s, win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
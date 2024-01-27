
class InvalidScreenshotException(Exception):
    def __init__(self, message="Provided screenshot is invalid.\n"):
        self.message = message
        super().__init__(self.message)


class InvalidScreenshotException(Exception):
    def __init__(self, message="Provided screenshot is invalid.\n"):
        self.message = message
        super().__init__(self.message)


class CorruptedConfigFileError(Exception):
    def __init__(self, message="The configuration file is corrupted."):
        self.message = message
        super().__init__(self.message)

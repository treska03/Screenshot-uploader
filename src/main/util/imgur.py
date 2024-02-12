import requests
from src.main.util.exceptions import InvalidScreenshotException

class API_Handler:

    def __init__(self, client_id):
        self.client_id = client_id

    def upload(self, screenshot):
        uri = 'https://api.imgur.com/3/image'
        header = {"Authorization": f'Client-ID {self.client_id}'} 
        data = screenshot

        r = requests.post(
            url=uri,
            headers=header,
            data=data    
        )

        if not r.ok:
            raise InvalidScreenshotException()
        
        return r.content
import requests

class Settings:
    def __init__(self):
        self.page_title = "Miguel Castaneda"
        self.layout = "wide"


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None    
    return r.json()
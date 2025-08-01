"""Wake up API from render.com"""
import requests

URL = 'https://eminem-quotes-api.onrender.com/'
def wake_api():
    try:
        requests.get(URL)
    except requests.exceptions.ConnectionError:
        pass
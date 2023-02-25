from dotenv import dotenv_values
import requests

class NewsFeed:
    """
    News feed model to generate news based on data
    """
    def __init__(self, data) -> None:
        self.data = data

    def get(self):
        url = ('https://newsapi.org/v2/everything?'
               'q=Apple&'
               'from=2023-02-23&'
               'sortBy=popularity&'
               f'apiKey={dotenv_values(".env")["NEWS_API_KEY"]}')
        res = requests.get(url)
        return res.json()

from dotenv import dotenv_values
import requests


class NewsFeed:
    """
    News feed model to generate news based on data
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = dotenv_values(".env")["NEWS_API_KEY"]
    def __init__(self, interest: str, language: str = "en") -> None:
        self.interest = interest
        self.language = language

    def get(self):
        news = []
        url = (
            f'{self.base_url}' 
            f'qInTitle={self.interest}&' 
            'from=2023-02-25&' 
            'sortBy=popularity&' 
            f'language={self.language}&'
            f'apiKey={self.api_key}'
           )
        res = requests.get(url)
        for article in res.json()['articles']:
            news.append({ "title": article['title'], "url": article['url'] })

        return news

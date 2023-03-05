import requests
from dotenv import dotenv_values
class Email:
    """
    Represents a email model
    """
    domain_name = dotenv_values(".env")["MAILGUN_DOMAIN"]
    api_key = dotenv_values(".env")["MAILGUN_API_KEY"]
    def __init__(self, to: str, body: str):
        self.to = to
        self.body = body
    def send_simple_message(self):
        """
        Implementation for sending out emails via https://www.mailgun.com/
        """
        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain_name}/messages",
            auth=("api", f'{self.api_key}'),
            data={"from": f"Excited User <mailgun@{self.domain_name}>",
                  "to": [self.to],
                  "subject": "Hello",
                  "text": self.body})
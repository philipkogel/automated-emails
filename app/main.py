"""
Main app file
"""
from models import NewsFeed, Email

nf = NewsFeed(interest="nasa")
news = nf.get()
example_email_body = ''
for n in news:
    example_email_body += n['title'] + '\n' + n['url'] + '\n\n'

email = Email(to='tafape7969@wwgoc.com', body=example_email_body)
req = email.send_simple_message()

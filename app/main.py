"""
Main app file
"""
from models import NewsFeed

nf = NewsFeed(interest="nasa")
news = nf.get()
example_email_body = ''
for n in news:
    example_email_body += n['title'] + '\n' + n['url'] + '\n\n'

print(example_email_body)

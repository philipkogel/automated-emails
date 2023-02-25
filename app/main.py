"""
Main app file
"""
from models import NewsFeed

nf = NewsFeed(data="books")
nf.get()

"""
Main app file
"""
import os
import requests


url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-02-23&'
       'sortBy=popularity&'
       'apiKey=c84e50fb61034866b66d2b3f7c3f087e')
res = requests.get(url)
print(res.json)

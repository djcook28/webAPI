import requests

api_key = 'd83f04ed1487474dbfe72e75c98d9d25'
url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d83f04ed1487474dbfe72e75c98d9d25'

request = requests.get(url)
content = request.json()
articles = content['articles']

for article in articles:
    print(article['description'])
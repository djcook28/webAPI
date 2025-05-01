import requests
import send_email

api_key = 'd83f04ed1487474dbfe72e75c98d9d25'
url = ('https://newsapi.org/v2/top-headlines?sources=techcrunch&api'
       'Key=d83f04ed1487474dbfe72e75c98d9d25&language=en')

request = requests.get(url)
content = request.json()
articles = content['articles']

body = ''

for article in articles[:20]:
    body = body + f"""{article['title']}
    {article['description']}
    {article['url']}
    
    """

send_email.send_email(body.encode("ascii", "ignore").decode(), "Daily News")

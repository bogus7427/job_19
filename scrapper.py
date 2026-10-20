import requests
from bs4 import BeautifulSoup

keyword ="파이썬"
r = requests.get('https://search.incruit.com/list/search.asp?col=all&src=gsw*search&kw=%C6%C4%C0%CC%BD%E3=파이썬')
r = requests.get(url)
print(r.text)
BeautifulSoup(r.text,"html.parser")

print(soup.prettify())
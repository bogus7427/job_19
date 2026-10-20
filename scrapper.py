import requests
from bs4 import BeautifulSoup

keyword ="파이썬"
url =f'https://search.incruit.com/list/search.asp?col=job&kw={keyword}'
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text,"html.parser")

#print(soup.prettify())

lis= soup.find_all("li", class_="c_col")
#print(lis)
#pirnt(len(lis))

for il in lis:
    try:
        company =il.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("a").text
        print(title)
    except:
        pass
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
jobs = []

for li in lis:
    try:
        company = li.find("a", class_="cpname").text
        title = li.find("div", class_="cell_mid").find("a").text
        locatiom = li.find("div", class_="cl_md").find_all("span")[0].text
        link = li.find("div", class_="cell_mid").find("a").get("href")

        job_dato = {
            "company": company,
            "title": title,
            "location" : locatiom,
            "link" : link
        }
        jobs.append(job_dato)
    except:
        pass
print(jobs)
print(len(jobs))


import requests
from bs4 import BeautifulSoup



def search_incruit(keyword, pages=1):
    jobs = []
    for i in range(pages):
        page = i * 30 

        url =f'https://search.incruit.com/list/search.asp?col=job&kw=startno=0={keyword}&startno={page}'
        r = requests.get(url)
        #print(r.text)
        soup = BeautifulSoup(r.text,"html.parser")

        #print(soup.prettify())

        lis= soup.find_all("li", class_="c_col")
        #print(lis)
        #pirnt(len(lis))
        print(f"{i+1}페이지 크롤링 중...")

        #jobs = []
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
    return jobs


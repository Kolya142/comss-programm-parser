import requests
from bs4 import BeautifulSoup as Soup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
f = open('sites.txt', 'w')
url0 = "https://www.comss.ru/page.php?id="
a = 0
while 1==1:
    url = (url0 + str(a))
    response = requests.get(url,headers=headers)
    soup = Soup(response.content, 'html.parser')
    title = soup.find("title")
    if not title.text == "Just a moment...":
        f.write(url + ": " + title.text + '\n')
        print("page: " + str(a))
    a += 1
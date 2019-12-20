import bs4
import requests
import re

url = "https://projecteuler.net"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,"html.parser")
#print(soup.prettify())
all_links = []
for links in soup.find_all("a"):
    link = links.get("href")
    all_links.append("https://projecteuler.net"+"/"+link)
print(all_links)

for headings in soup.find_all("p"):
        print(head.text)
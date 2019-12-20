import urllib.request
import http.cookiejar
import requests
import bs4

friend=[]
z = 0
cj = http.cookiejar.CookieJar()
def main():

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    url = "https://m.facebook.com/login.php"
    payload = {
        "email":"yourEmail",
        "pass":"yourPassword"
        }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req)
    cont = resp.read()
def get_data(url):
    data = requests.get(url,cookies = cj)
    soup = bs4.BeautifulSoup(data.text,"html.parser")
    return soup
z = 0
main()
fname = "rahulbhatia12344"
soup = get_data(url = "https://m.facebook.com/{}/friends".format(fname))
for i in range(4):
    z = 0
    for name in soup.find_all("a"):
        if name.text !="Add Friend" and z > 17:
            if name.text.lower() =="see more friends":
                next_tab = str(name)[9:192]
                break
            friend.append(name.text)
        z+=1
    soup = get_data(url="https://m.facebook.com" + next_tab)
print(friend)
print(len(friend))

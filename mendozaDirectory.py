
from bs4 import BeautifulSoup

with open("directory.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")
    for professorInfo in soup.find_all("div",class_="directory-content"):
        print('-')
        for i in professorInfo.find_all("a","a-profile",href=True):
            print(i.text)
        print('-')
        
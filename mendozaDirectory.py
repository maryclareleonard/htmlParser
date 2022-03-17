from bs4 import BeautifulSoup

allInfoDoc = open("professorsAndEmails.txt","x")
emailOnlyDoc = open("emails.txt","x")

with open("directory.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")
    for professorInfo in soup.find_all("div",class_="directory-content"):
        
        for nameDepartEmail in professorInfo.find_all("a","a-profile",href=True):
            for individualDetail in nameDepartEmail:
                allInfoDoc.write(individualDetail)
                if individualDetail.endswith('nd.edu'):
                    emailOnlyDoc.write(individualDetail)
                    emailOnlyDoc.write("\n")
                allInfoDoc.write("\n")
        allInfoDoc.write("\n")



        
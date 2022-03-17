from bs4 import BeautifulSoup

allInfoDoc = open("staffAndEmails.txt","x")
emailOnlyDoc = open("staffEmailsOnly.txt","x")

with open("staffDirectory.html") as fp:
    soup = BeautifulSoup(fp,"html.parser")
    for staffInfo in soup.find_all("div",class_="directory-content"):
        
        for nameDepartEmail in staffInfo.find_all("a","a-profile",href=True):
            for individualDetail in nameDepartEmail:
                allInfoDoc.write(individualDetail)
                if individualDetail.endswith('nd.edu'):
                    emailOnlyDoc.write(individualDetail)
                    emailOnlyDoc.write("\n")
                allInfoDoc.write("\n")
        allInfoDoc.write("\n")
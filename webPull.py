import requests
from bs4 import BeautifulSoup
import re

url = "https://callink.berkeley.edu/api/discovery/search/organizations?orderBy%5B0%5D=UpperName%20asc&top=1482&filter=&query=&skip=0"

response = requests.get(url)
data = response.json()

organizations = data["value"]
clubUrls = []

for org in organizations:
    clubUrls.append("https://callink.berkeley.edu/organization/" + org["WebsiteKey"])

for url in clubUrls:

    response = requests.get(url)
    if response.status_code != 200:
        print("Error: " + str(response.status_code))
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    email_regex = r'"email":"([^"]*)"'
    email = re.findall(email_regex, str(soup))

    name_regex = r'"name":"([^"]*)"'
    name = re.findall(name_regex, str(soup))

    if len(email) == 0:
        email = ["No email found"]
        continue

    if len(name) == 0:
        name = ["No name found"]
        continue
    
    print(name[0] + ": " + email[0])

else:
    print("Failed to retrieve the Webpage")

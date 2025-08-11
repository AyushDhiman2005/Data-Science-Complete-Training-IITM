'''
 Government Jobs Scraper
 Search for "Government Jobs 2025" on Google
 Save top 10 results in a text file
 Use requests and file handling

'''

import requests as r
from bs4 import BeautifulSoup


url=r'https://www.indgovtjobs.in/2015/10/Government-Jobs.html#google_vignette'
responses = r.get(url)


soup = BeautifulSoup(responses.text)



result=[]


for x in soup.find_all('tr'):
    result.append(x)

print(result)
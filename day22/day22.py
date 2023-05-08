#web scraping, that's cool


import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)

content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
#print(soup.body)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
#for td in table.find('tr').find_all('td'):
#    print(td.text)

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
print(response.status_code)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all("div", {"class":"facts-wrapper"})
print(tables)

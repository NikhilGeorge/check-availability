import requests
from bs4 import BeautifulSoup

def parse(url, class_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    return links

links = parse("https://www.tpbazaar.com/posts?PostSearch%5Bcategory%5D=7&PostSearch%5Btech_park_id%5D=2", "introduction")

for link in links:
    print(link.get('href'))



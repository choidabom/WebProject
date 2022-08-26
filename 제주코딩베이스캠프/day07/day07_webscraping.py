import requests
from bs4 import BeautifulSoup

response = requests.get('https://ridibooks.com/category/free-books/2200')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup.title)                      # title 태그 출력
# print(soup.find('title'))              # title 태그 출력
# print(soup.find(id='content'))         # id 가 'content'인 태그 출력

# print(soup.find_all('a'))              # 모든 a 태그 출력
# print(soup.select('#content'))         # id 가 'content'인 모든 태그 출력 
# print(soup.select('.container > a'))   # 'container' class 안에 모든 a 태그 출력
data = soup.select('.title_text')

for i in enumerate(data):
    print(i, data.text.strip())
    
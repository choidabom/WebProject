import requests
import re
from bs4 import BeautifulSoup
import csv
url = "https://search.shopping.naver.com/~~~"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select("#productListArea > ul > li")
powerbanklist = [] # 리스트 생성
# print(items)

for item in items:
    temp=[]
    name = item.select_one("#productListArea > ul > li > p > a")["title"]
    price = item.select_one("#productListArea > ul > li > div.price > strong > span.num").text
    link = itme.select_one("#productListArea > ul > li > p > a")["href"]
    review_number = item.select_one("#productListArea > ul > li > div.info > span > a.txt > em").text
    review_number = review_number[1:-1]
    # print(review_number)
    temp.append(name)
    temp.append(price)
    temp.append(link)
    temp.append(review_number)
    powerbanklist.append(temp)

with open('powerbanklist_select.csv', "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['품명', '링크', '가격', '리뷰수'])
    writer.writerows(powerbanklist)
f.close

# 웹 스크래핑 해보기
# 네이버 영화 순위 페이지에서 영화 제목 뿐만 아니라 순위, 별점을 스크래핑
# 링크: https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303

import requests
from bs4 import BeautifulSoup

# 타켓 URL을 읽어서 HTML를 받아옴
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
soup = BeautifulSoup(data.text, 'html.parser') 

# 위에서 파악한 구조를 이용하여 select()을 이용하여 영화를 찾는다.
movies = soup.select('#old_content > table > tbody > tr')
    
# movies 반복문 돌리기
for movie in movies:
    title = movie.select_one('td.title > div > a') # tr안에 a가 있으면,

    if title is not None:
        # 순위 => #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        rank = movie.select_one("td:nth-child(1) > img")['alt']

        # 평점 => #old_content > table > tbody > tr:nth-child(2) > td.point
        point = movie.select_one("td.point")
        
        print(rank, title.text, point.text)

# 태그 안의 텍스트를 찍고 싶을 땐 -> 태그.text
# 태그 안의 속성을 찍고 싶을 땐 -> 태그['속성']
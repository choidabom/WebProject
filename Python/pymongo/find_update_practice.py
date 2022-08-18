# - 위의 코드는 실행할 때마다 50개의 영화정보가 계속 쌓일 것이므로,
#  다른 파이썬 파일을 새로 하나 만들어 find, update를 연습해보겠습니다.

# pymongo 기본 코드
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

# Q1. 영화제목 '매트릭스'의 평점을 가져오기
target_movie = db.movies.find_one({'title': '매트릭스'})
target_start = target_movie['star']
print(target_start)

# Q2. '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
movies = list(db.movies.find({'star':target_start}))

for movie in movies:
    print(movie['title'])

# Q3. 매트릭스 영화의 평점을 0으로 만들기
change_rank = db.movies.update_one({'title':'매트릭스'}, {'$set':{'star':'0'}})
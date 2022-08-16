# 서울시 대기 OpenAPI에서 미세먼지 정보

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

# print(rjson)
print(rjson['RealtimeCityAir']['row'][0]['NO2']) # 중구의 NO2 값


# 모든 구의 IDEX_MVL 값 프린트하기
gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

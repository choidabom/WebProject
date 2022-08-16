# Q1. 과일 갯수 세기 함수 만들기
# 과일 이름이 들어있는 리스트가 있을 때, 특정 과일이 몇 개 들어있는지 세는 함수

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# 사과의 갯수 세기

# count = 0
# for fruit in fruits:
#     if fruit == '사과'
#         count += 1

# print(count) 

# 사과가 아닌 다른 과일에 대해서도 쓸 수 있도록 함수 만들기

def count_fruits(target):
    count = 0
    for fruit in fruits:
        if fruit == target:
            count += 1
    return count

subak_count = count_fruits('수박')
print(subak_count)

gam_count = count_fruits('감')
print(gam_count)
# 사람의 나이 출력하기
# 각 사람의 이름과 나이가 든 딕셔너리가 각각의 요소인 리스트가 있을 때, 
# 이름을 넣으면 나이를 돌려주는 함수를 만들어보라.

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]


def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('kay'))
# 클래스는 찍어내는 틀(붕어빵 찍는 틀, 생산품을 만들어내는 공장)
    # 클래스 안에 변수: 멤버
    # 클래스 안에 함수: 메서드

# 인스턴스는 찍어져 나온 결과물

class Car:
    all_car = []    # 클래스 변수
    def __init__(self, name):
        self.instance_name = name   # 인스턴스 변수
        self.all_car.append(self.instance_name)
        print('인스턴스 생성!')

    def __str__(self):  # 매직메서드 : 해당 자료형에 속성
        return self.instance_name

    maxSpeed = 300
    maxPeople = 5
    
    def start(self):
        print('출발합니다.')
    def stop(self):
        print('멈춥니다.')

# self는 어찌됐건 공유되는 메모리를 가리킨다.

a = Car('붕붕카')
b = Car('카봇')
c = Car('카')

a.maxSpeed
a.start()

type(a), dir(a)
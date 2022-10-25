# 차 클래스 정의
class Car:
    def __init__(self, maker, model, color, year):
        self.maker = maker
        self.model = model
        self.color = color
        self.year = year

    def __repr__(self):
        return f'{self.model}{self.year, self.maker, self.color}'


# 인스턴스 생성 및 값 확인
car_shed = [
    Car('페라리', '푸로산게', '빨강색', 2022),
    Car('현대', '아이오닉6', '흰색', 2023),
    Car('기아', 'EV6', '회색', 2021),
    Car('제네시스', 'GV70', '검정', 2020),
]
print(car_shed)
print(car_shed[0])
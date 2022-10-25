# 차 클래스 정의
class Car:
    def __init__(self, maker, model, color, year, max_fuel, fuel = 0):
        self.maker = maker
        self.model = model
        self.color = color
        self.year = year
        self.max_fuel = max_fuel
        self.fuel = fuel

    def __repr__(self):
        return f'{self.model}{self.year, self.maker, self.color}'

    def charge_fuel(self, fuel):
        prev_fuel = self.fuel
        self.fuel += fuel
        if self.fuel > self.max_fuel:
            self.fuel = self.max_fuel
        print(f'[충전] : {prev_fuel} >>> {self.fuel}')


# 인스턴스 생성 및 값 확인
car1 = Car('페라리', '푸로산게', '빨강색', 2022, 100)
print(car1)
car1.charge_fuel(40)
car1.charge_fuel(40)
car1.charge_fuel(40)


# 붕어빵 클래스 정의
class FishShapedBun:
    def __init__(self, ingredient):
        self.stuffing = ingredient

    def __repr__(self):
        return f'{self.stuffing} 붕어빵'


# 인스턴스 생성 및 값 확인
buns = [FishShapedBun('팥'), FishShapedBun('슈크림')]
print(buns)  # 리스트를 출력
print(buns[0])  # 하나의 데이터만 출력
print(buns[1])  # 하나의 데이터만 출력
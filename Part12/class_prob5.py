# 붕어빵 클래스 정의
class FishShapedBun:
    def __init__(self, ingredient):
        self.stuffing = ingredient


# 인스턴스 생성 및 값 확인
bun = FishShapedBun('팥')
print(isinstance(bun, int))  # type이 int 인가?
print(isinstance(bun, FishShapedBun))  # type이 FishShapeBun 인가?
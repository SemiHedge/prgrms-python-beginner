'''
함수 만들기 실습 (1)
> 다소 어려울 수 있는 문제입니다.

슬프게도(?) 표준체중과 비만도 계산식은 다음과 같다고 한다.

1. 표준체중(kg) = (현재신장cm - 100) X 0.9
2. 비만도(%) = (현재체중 ÷ 표준체중) X 100

| 판정 | BMI 값 |
| --- | --- |
| 저체중 | 80미만 |
| 정상체중 | 90이상 110미만 |
| 과체중 | 110이상 120미만 |


이 때 BMI 값을 계산하는 함수 `solution(height, weight)`를 구현합시다

* height : 키(단위 cm), weight : 몸무게(단위 kg)
* 최종 BMI값은 자연수로 변환하여 반환합니다. 따라서 `int()` 또는 내림처리합니다.
    * 예시1 : 123.4444 -> 123
    * 예시2 : 40.9 -> 40

- - -

### 입출력 예시

| height | weight | bmi |
| --- | --- | --- |
| 177 | 70 | 101 |
| 180 | 62 | 86 |
| 190 | 101 | 124 |
'''
# 표준체중(kg) = (현재신장cm - 100) X 0.9
# 비만도(%) = (현재체중 ÷ 표준체중) X 100
def solution(height, weight):
    standard = (height - 100) * 0.9
    bmi = int((weight / standard) * 100)
    if bmi < 80:
        return bmi, '저체중'
    elif 80 <= bmi < 110:
        return bmi, '정상체중'
    else:
        return bmi, '과체중'

print(solution(177, 70))
print(solution(180, 55))
print(solution(190, 101))
print(solution(150, 45))
print(solution(160, 55))
print(solution(165, 75))


import unittest

class MyTest(unittest.TestCase):
    def test(self):
        try:
            self.assertEqual(solution(177, 70), (101, '정상체중'))
            print("(177, 70) -> (101, '정상체중') : 정답입니다.") # 맞으면 출력할 메시지
        except:
            print(f"(177, 70) -> {solution(177, 70)} : 틀렸습니다. 기대값 : (101, '정상체중')")
            self.assertTrue(False)
        try:
            self.assertEqual(solution(180, 55), (76, '저체중'))
            print("(180, 55) -> (76, '저체중') : 정답입니다.") # 맞으면 출력할 메시지
        except:
            print(f"(180, 55) -> {solution(180, 55)} : 틀렸습니다. 기대값 : (76, '저체중')")
            self.assertTrue(False)
        try:
            self.assertEqual(solution(190, 101), (124, '과체중'))
            print("(190, 101) -> (124, '과체중') : 정답입니다.") # 맞으면 출력할 메시지
        except:
            print(f"(190, 101) -> {solution(190, 101)} : 틀렸습니다. 기대값 : (124, '과체중')")
            self.assertTrue(False)

        

    def test(self):
        # a, b의 합을 반환하는 함수를 작성하는 문제일 때
        
        self.assertEqual(solution(177, 70), (101, '정상체중'))
        self.assertEqual(solution(180, 55), (76, '저체중'))
        self.assertEqual(solution(190, 101), (124, '과체중'))
        self.assertEqual(solution(150, 45), (100, '정상체중'))
        self.assertEqual(solution(160, 55), (101, '정상체중'))
        self.assertEqual(solution(165, 75), (128, '과체중'))
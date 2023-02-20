# 표준체중(kg) = (현재신장cm - 100) X 0.9
# 비만도(%) = (현재체중 ÷ 표준체중) X 100
def calc_bmi(height, weight):
    standard = (height - 100) * 0.9
    bmi = (weight / standard) * 100
    return int(bmi)

print(calc_bmi(177, 70))
print(calc_bmi(180, 62))
print(calc_bmi(190, 101))
print(calc_bmi(150, 45))
print(calc_bmi(160, 55))
print(calc_bmi(165, 75))


import unittest

class MyTest(unittest.TestCase):
    def test(self):
				# a, b의 합을 반환하는 함수를 작성하는 문제일 때
        self.assertEqual(solution(177, 70), 101)
        self.assertEqual(solution(180, 55), 76)
        self.assertEqual(solution(190, 101), 124)
        self.assertEqual(solution(150, 45), 100)
        self.assertEqual(solution(160, 55), 101)
        self.assertEqual(solution(165, 75), 128)
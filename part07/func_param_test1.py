# 적절한 매개변수 설정하기
def power(x, y = 2):
    return x ** y


# 거듭 제곱하는 함수
print(power(2))  # 2 * 2 = 4
print(power(3))  # 3 * 3 = 9
print(power(4, 5))  # 4 * 4 * 4 * 4 * 4 = 1024
print(power(4, 3))  # 4 * 4 * 4 = 64

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(power(2), 4)
        self.assertEqual(power(3), 9)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 5), 1024)
        self.assertEqual(power(4, 3), 64)
        self.assertEqual(power(6, 3), 216)
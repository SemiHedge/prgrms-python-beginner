# 적절한 매개변수 설정하기
def make_coffee(item, bean, temperature = 'hot', caffeine = True):
    return item, bean, temperature, caffeine


# 함수 실행
print(make_coffee('아메리카노', '브라질'))  # ('아메리카노', '브라질', 'hot', True)
print(make_coffee('아메리카노', '콜롬비아', 'ice'))  # ('아메리카노', '콜롬비아', 'ice', True)
print(make_coffee('카페라떼', '케냐', 'ice', False))  # ('카페라떼', '케냐', 'ice', False)
print(make_coffee('카푸치노', '에티오피아', caffeine = False))  # ('카푸치노', '에티오피아', 'hot', False)
print(make_coffee('콜드브루', '하와이안', temperature = 'ice'))  # ('콜드브루', '하와이안', 'ice', True)

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(make_coffee('아메리카노', '브라질'), ('아메리카노', '브라질', 'hot', True))
        self.assertEqual(make_coffee('아메리카노', '콜롬비아', 'ice'), ('아메리카노', '콜롬비아', 'ice', True))
        self.assertEqual(make_coffee('카페라떼', '케냐', 'ice', False), ('카페라떼', '케냐', 'ice', False))
        self.assertEqual(make_coffee('카푸치노', '에티오피아', caffeine = False), ('카푸치노', '에티오피아', 'hot', False))
        self.assertEqual(make_coffee('콜드브루', '하와이안', temperature = 'ice'), ('콜드브루', '하와이안', 'ice', True))

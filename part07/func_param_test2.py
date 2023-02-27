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
        judge = True

        # case 1
        try:
            self.assertEqual(make_coffee('아메리카노', '브라질'), ('아메리카노', '브라질', 'hot', True))
            print(f"[정답] 입력 : ('아메리카노', '브라질') 출력값 : {make_coffee('아메리카노', '브라질')} | 기대값 : ('아메리카노', '브라질', 'hot', True)") # 맞으면 출력할 메시지
        except:
            print(f"[오답] 입력 : ('아메리카노', '브라질') 출력값 : {make_coffee('아메리카노', '브라질')} | 기대값 : ('아메리카노', '브라질', 'hot', True)")
            judge = False

        # case 2
        try:
            self.assertEqual(make_coffee('아메리카노', '콜롬비아', 'ice'), ('아메리카노', '콜롬비아', 'ice', True))
            print(f"[정답] 입력 : ('아메리카노', '콜롬비아', 'ice') 출력값 : {make_coffee('아메리카노', '콜롬비아', 'ice')} | 기대값 : ('아메리카노', '콜롬비아', 'ice', True)") # 맞으면 출력할 메시지
        except:
            print(f"[오답] 입력 : ('아메리카노', '콜롬비아', 'ice') 출력값 : {make_coffee('아메리카노', '콜롬비아', 'ice')} | 기대값 : ('아메리카노', '콜롬비아', 'ice', True)")
            judge = False

        # case 3
        try:
            self.assertEqual(make_coffee('카페라떼', '케냐', 'ice', False), ('카페라떼', '케냐', 'ice', False))
            print(f"[정답] 입력 : ('카페라떼', '케냐', 'ice', False) 출력값 : {make_coffee('카페라떼', '케냐', 'ice', False)} | 기대값 : ('카페라떼', '케냐', 'ice', False)") # 맞으면 출력할 메시지
        except:
            print(f"[오답] 입력 : ('카페라떼', '케냐', 'ice', False) 출력값 : {make_coffee('카페라떼', '케냐', 'ice', False)} | 기대값 : ('카페라떼', '케냐', 'ice', False)")
            judge = False
        
        # case 4
        try:
            self.assertEqual(make_coffee('카푸치노', '에티오피아', caffeine = False), ('카푸치노', '에티오피아', 'hot', False))
            print(f"[정답] 입력 : ('카푸치노', '에티오피아', caffeine = False) 출력값 : {make_coffee('카푸치노', '에티오피아', caffeine = False)} | 기대값 : ('카푸치노', '에티오피아', 'hot', False)") # 맞으면 출력할 메시지
        except:
            print(f"[오답] 입력 : ('카푸치노', '에티오피아', caffeine = False) 출력값 : {make_coffee('카푸치노', '에티오피아', caffeine = False)} | 기대값 : ('카푸치노', '에티오피아', 'hot', False)")
            judge = False
        
        # case 5
        try:
            self.assertEqual(make_coffee('콜드브루', '하와이안', temperature = 'ice'), ('콜드브루', '하와이안', 'ice', True))
            print(f"[정답] 입력 : ('콜드브루', '하와이안', temperature = 'ice') 출력값 : {make_coffee('콜드브루', '하와이안', temperature = 'ice')} | 기대값 : ('콜드브루', '하와이안', 'ice', True)") # 맞으면 출력할 메시지
        except:
            print(f"[오답] 입력 : ('콜드브루', '하와이안', temperature = 'ice') 출력값 : {make_coffee('콜드브루', '하와이안', temperature = 'ice')} | 기대값 : ('콜드브루', '하와이안', 'ice', True)")
            judge = False


        # final judge
        self.assertTrue(judge)

    """
    def test(self):
        self.assertEqual(make_coffee('아메리카노', '브라질'), ('아메리카노', '브라질', 'hot', True))
        self.assertEqual(make_coffee('아메리카노', '콜롬비아', 'ice'), ('아메리카노', '콜롬비아', 'ice', True))
        self.assertEqual(make_coffee('카페라떼', '케냐', 'ice', False), ('카페라떼', '케냐', 'ice', False))
        self.assertEqual(make_coffee('카푸치노', '에티오피아', caffeine = False), ('카푸치노', '에티오피아', 'hot', False))
        self.assertEqual(make_coffee('콜드브루', '하와이안', temperature = 'ice'), ('콜드브루', '하와이안', 'ice', True))
    """
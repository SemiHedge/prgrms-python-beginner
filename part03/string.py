# Text - string(문자열)
text1 = '안녕하세요.'
text2 = "프로그래머스입니다."
text3 = "스펜서는 '이렇게 작은따옴표' 라고 말했다."
text4 = '머쓱이는 "이렇게 큰따옴표" 라고 말했다.'
text5 = """
이렇게 하면
장문의 머쓱이 편지를
쓸 수 있습니다.
"""

print(text1, text2, text3, text4, text5)

print(text1 + text2)

# 특수 문자(escape 문자 \)
# \n \t \\ \' \" \0
text6 = 'abc\ndef'
print(text6)

text7 = 'Mussg\'s favorite food is bugs in Python'
print(text7)
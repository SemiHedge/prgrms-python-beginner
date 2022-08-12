# string function
# upper
from prompt_toolkit import print_formatted_text


text = "AbCdE"
text = text.upper()
print(text)


# lower
text = "AbCdE"
text = text.lower()
print(text)


# count
cnt_c = "aCbCdCeC".count('C')
print(cnt_c)


# isalpha - 알파벳 체크
text = "10 years old"
check = text.isalpha()
print(check)


# isnumeric() - 숫자만 체크
text = "2022"
check = text.isnumeric()
print(check)


# isalnum() - 문자 숫자로만 이루어졌는제 체크
text1 = "10 years old".isalnum()
text2 = "10살입니다".isalnum()
print(text1, text2)


# ljust rjust center
text1 = "Hello".ljust(10)
text2 = "Hello".rjust(10)
text3 = "Hello".center(10)
print_formatted_text(text1, text2, text3)
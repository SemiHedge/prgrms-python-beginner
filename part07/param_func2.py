def to_greeting():
    user = "스펜서"
    print("안녕하세요!")
    print(f"오랜만이네요 {user}")
    print("오늘 좋은 하루 되길 바라요~")


to_greeting()


def to_greeting(user):
    print("안녕하세요!")
    print(f"오랜만이네요 {user}")
    print("오늘 좋은 하루 되길 바라요~")


to_greeting('스펜서')
to_greeting('머쓱이')
to_greeting(user = '머쓱이')

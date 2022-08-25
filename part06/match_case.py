# match_case.py 3.10~
# switch/case문
status = 200

match status:
    case 200:
        print(f"{status} Success")
    case 300:
        print(f"{status} Redirect")
    case 400:
        print(f"{status} Client Error")
    case 500:
        print(f"{status} Server Error")
    case _:
        print(f"{status} 해당사항이 없습니다.")
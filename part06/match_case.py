# python 3.10
status = 303
match status:
    case 200:
        print("success")
    case 300:
        print("redirect")
    case 400:
        print("client error")
    case 500:
        print("server error")
    case _:
        print("not match")
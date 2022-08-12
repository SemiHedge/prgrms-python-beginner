def purchase_price():
    new_price = 50000 * (100 - 20) / 100
    new_price = int(new_price)
    print(f'구매 가격은 {new_price}원 입니다.')


purchase_price()

def purchase_price(price, per):
    new_price = price * (100 - per) / 100
    new_price = int(new_price)
    print(f'구매 가격은 {new_price}원 입니다.')


# 실행
purchase_price(10000, 10)
purchase_price(5000, 33)

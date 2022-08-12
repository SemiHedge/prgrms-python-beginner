def purchase_price(price, per):
    new_price = price * (100 - per) / 100
    new_price = int(new_price)
    print(f'구매 가격은 {new_price}원 입니다.')


# 실행
p1 = purchase_price(10000, 10)
p2 = purchase_price(5000, 33)
print(p1, p2)  # None None
# print(p1 + p2)  # error
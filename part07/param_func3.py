# 쇼핑몰 할인율 -> 구매가격
# 할인가가 적용된 상품 가격 얻는 함수
def purchase_price(price, sale_per):
    new_price = price * (100 - sale_per) / 100
    new_price = int(new_price)
    print(f"구매 가격은 {new_price} 입니다.")


# 함수 실행
purchase_price(20000, 50)
purchase_price(40000, 20)
# *args **kwargs
def check_basket(**item):
    print(f'장바구니 상황 : {item}')



check_basket(breakfast='사과', lunch='고기', dinner='삶은계란')
{'breakfast': '사과', 'lunch': '고기', 'dinner': '삶은계란'} # dict
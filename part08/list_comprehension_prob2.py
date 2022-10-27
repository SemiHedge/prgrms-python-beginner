# 환율 반영 하기
exchange_rate_us = 0.71
wallets_kr = [20000, 30000, 50000, 70000, 5000]

# 리스트 컴프리헨션으로 us 환율로 변환
wallets_us = [x * exchange_rate_us for x in wallets_kr]

# 출력
print(wallets_us)
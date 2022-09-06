import time

print("start")
time.sleep(2)
print("end")

start = time.time() # 유닉스시간 UTC 1970.1.1 00:00:00부터의 초
print(start)

# 시간 측정
start = time.time()
total = 0
for i in range(10000001):
    total += i
    print(total)
print(total, time.time()-start)

# n, n-1, n-2, ...,  1, 0
import time
def countdown(number):
    print(number)
    time.sleep(1)
    if number == 0:
        return
    else:
        return countdown(number-1)

countdown(10)
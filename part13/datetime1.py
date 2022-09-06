# from datetime import date, time, datetime, timedelta
from datetime import datetime, timedelta, timezone
# 지금 이순간
now = datetime.now()
print(now, type(now))

# 특정 시간대
future = datetime(2200, 11, 18)
print(future)

# 시간 - 시간 = 시간차이(timedelta)
interval = future - now
print(interval, type(interval))

# 시간차 (timedelta)
period = timedelta(days=365)
print(now+period)
# month, year는 매번 달라질 수 있으니 제외

# 날짜 포맷 - 대소소대대대
date1 = now.strftime("%Y %m %d %p %I %H %M %S %A %a")
date2 = now.strftime("%Y년 %m %d %p %I %H:%M:%S")
print(date1)
print(date2)
# https://docs.python.org/ko/3/library/datetime.html#strftime-and-strptime-format-codes


# 국가 시간 설정 UTC 미국 LA UT-7:00, 한국 UTC+09:00
nz_tz = timezone(timedelta(hours=-7))  
nz_now = datetime.now(tz=nz_tz)
print(nz_now)
print(now)
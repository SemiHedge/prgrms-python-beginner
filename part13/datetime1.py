# import datetime
# now = datetime.datetime.now()
# print(now)

# 현재시각!
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now, type(now))

# 시각 - 시각 = 시간차이(timedelta)
future = datetime(2200, 11, 18)
print(future)
interval = future - now
print(interval, type(interval))

# 시간차이
period = timedelta(days=1000, hours=10)
print(period)
print(now - period)

# 시간 원하는 포맷(문자열)
print(f'{now.hour}:{now.minute}')
date1 = now.strftime("%Y %m %d %p %I %H %M %S %A")
date2 = now.strftime("%Y년 %m월 %d일 %p %I:%M:%S %a")
print(date2)

# 국가 시간 미국 LA -7 한국 0900
nz_tz = timezone(timedelta(hours=-7))
nz_now = datetime.now(tz=nz_tz)
print(nz_now)
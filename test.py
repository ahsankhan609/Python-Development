from datetime import datetime

n : int = 100000000 #if we use _ interpreter will ignore it
print(n)
print(f'{n:_}')
print(f'{n:,}')

now: datetime = datetime.now()
print(f'{now:%d. %m %y (%H:%M:%S)}')
print(f'{now:%c}')# return local datetime
print(f'{now:%I%p}')# return 24HRS time 
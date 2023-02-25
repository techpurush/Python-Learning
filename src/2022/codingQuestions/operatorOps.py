from collections import deque

d=deque([1,2,3,4])
print(
d.pop()
)

from datetime import datetime
s='Sun 10 May 2015 13:54:36 -0700'
# datetime.strptime(s,'')
dt=datetime.today()
print(dt.strftime('%z'))
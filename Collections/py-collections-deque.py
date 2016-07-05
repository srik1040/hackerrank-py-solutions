# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(raw_input())
d = deque()

for _ in range(N):
    data = raw_input().split()
    if len(data) > 1:
        cmd, args = data
        getattr(d, cmd)(args)
    else:
        cmd = data[0]
        getattr(d, cmd)()
for i in d:
    print i,
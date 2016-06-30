n = int(input())
s = set(map(int, input().split())) 

N = int(input())

for _ in range(N):
    command, *args = input().split()
    args = map(int, args)
    getattr(s, command)(*args)
    
print(sum(s))
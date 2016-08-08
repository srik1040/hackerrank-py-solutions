# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, raw_input().split())
data = list()
for _ in range(N):
    data.append(map(int, raw_input().split()))
K = int(raw_input())
data.sort(key=lambda x: x[K])
for i in data:
    print " ".join(map(str, i))
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = raw_input().split()
k = int(k)
data = []
for i in range(1, k+1):
    for j in map(lambda combination: ''.join(combination), combinations(sorted(S), i)):
        print j
    
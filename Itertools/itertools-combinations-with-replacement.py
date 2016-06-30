# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S, k = raw_input().split()
k = int(k)
data = []

for j in map(lambda combination: ''.join(combination), combinations_with_replacement(sorted(S), k)):
    print j
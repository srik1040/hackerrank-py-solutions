# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = map(int, raw_input().split())
B = map(int, raw_input().split())

for i in product(A, B):
    print i,

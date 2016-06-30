# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def int_list():
    return map(int, raw_input().split())

def compute_sum(ncount, subset):
    return sum(map(lambda number: ncount[number] if number in subset else 0, ncount))

n, m = int_list()
ncount = collections.defaultdict(int)
for number in int_list():
    ncount[number] += 1

A = set(int_list())
B = set(int_list())

print compute_sum(ncount, A) - compute_sum(ncount, B)
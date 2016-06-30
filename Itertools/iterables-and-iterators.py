# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import division
import itertools

N = int(raw_input())
S = raw_input().split()
K = int(raw_input())

combinations = list(itertools.combinations(S, K))
print len(list(filter(lambda x: 'a' in x, combinations))) / len(combinations)
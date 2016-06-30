# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, K = raw_input().split()
for i in sorted(list(permutations(S, int(K)))):
    print "".join(i)
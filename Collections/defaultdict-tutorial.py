# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n, m = map(int, raw_input().split())
    
wIndices = collections.defaultdict(list)
for i in range(n):
    wIndices[raw_input()].append(i + 1)

for i in range(m):
    word = raw_input()
    if wIndices[word]:
        print " ".join(str(x) for x in wIndices[word])
    else:
        print -1
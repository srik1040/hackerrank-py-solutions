# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

S = list(raw_input())
for item in sorted(collections.Counter(S).items(), key=lambda item: (-item[1], item[0]))[:3]:
    print "%s %d" % (item)
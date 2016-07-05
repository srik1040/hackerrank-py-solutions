# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

N = int(raw_input())
words = collections.OrderedDict()
for _ in range(N):
    word = raw_input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print len(set(words.keys()))
for i in words.values():
    print i,
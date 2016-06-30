# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
distinct_countries = set()

for _ in range(N):
    ctry = raw_input()
    distinct_countries.add(ctry)

print len(distinct_countries)


# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n = int(raw_input())
data = collections.defaultdict(str)
for i in range(n):
    country = raw_input()
    if country in data:
        pass
    else:
        data[country] = 1
        
print sum(data.values())
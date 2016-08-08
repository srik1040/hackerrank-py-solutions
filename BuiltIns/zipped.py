# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, raw_input().split())
data = list()
for _ in range(X):
    data.append(map(float, raw_input().split()))
for i in zip(*data):
    print "{0:.1f}".format(float(sum(i))/len(i))
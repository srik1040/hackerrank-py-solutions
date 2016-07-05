# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
def read_in():
    data = raw_input().split()
    return " ".join(data[:-1]), int(data[-1])
    
N = int(raw_input())
data = OrderedDict()
for _ in range(N):
    item_name, price = read_in()
    if item_name in data:
        data[item_name] += price
    else:
        data[item_name] = price

for key, val in data.items():
    print key, val
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

def read_in():
    return map(int, raw_input().split())

shoes = int(raw_input())
shoe_sizes = collections.Counter(read_in())
tot_money = 0
for _ in range(1, int(raw_input()) + 1):
    shoe_size, price = read_in()
    if shoe_size in shoe_sizes and shoe_sizes[shoe_size]:
        shoe_sizes[shoe_size] -= 1
        tot_money += price
print tot_money
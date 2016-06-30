# Enter your code here. Read input from STDIN. Print output to STDOUT
item_len = int(raw_input())
T = tuple(map(int, raw_input().split()))
print hash(T)
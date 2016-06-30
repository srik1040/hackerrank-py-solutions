# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = map(int, raw_input().split())
print sorted(set(A))[-2]
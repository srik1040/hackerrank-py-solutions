# Enter your code here. Read input from STDIN. Print output to STDOUT
tot_heights = float(raw_input())
heights = set(map(int, raw_input().split()))
tot_heights = float(len(heights))

print sum(heights)/tot_heights
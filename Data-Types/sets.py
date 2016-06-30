# Enter your code here. Read input from STDIN. Print output to STDOUT
M = raw_input()
setM = set(raw_input().split())
N = input()
setN = set(raw_input().split())

for i in sorted(map(int, setM.symmetric_difference(setN))):
    print i
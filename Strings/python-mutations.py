# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()
i, c = raw_input().split()
i = int(i)
print(S[:i] + c + S[i + 1:])
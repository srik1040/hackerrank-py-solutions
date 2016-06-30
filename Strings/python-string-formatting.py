# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
width = len(bin(N)[2:])
for i in range(1, N+1):
    print ' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[1:], hex(i)[2:].upper(), bin(i)[2:]]))
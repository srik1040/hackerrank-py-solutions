# Enter your code here. Read input from STDIN. Print output to STDOUT
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

print map(lambda x: fib(x) ** 3, range(int(raw_input())))
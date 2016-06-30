# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def read_int():
    return map(int, raw_input().split())

K, M = read_int()

lists = [list(read_int())[1:] for _ in range(K)]
print (max(map(lambda combination: sum(map(lambda x: x * x, combination)) % M, itertools.product(*lists))))
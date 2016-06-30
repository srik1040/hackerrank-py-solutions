def read_in():
    return set(map(int, input().split()))

A = read_in()
N = int(input())
sets = [read_in() for _ in range(N)]
print('True' if all(map(lambda s: A.union(s) == A and A!= s, sets)) else 'False')




def read_int():
    return set(map(int, input().split()))

A = read_int()
output = set()
for _ in range(int(input())):
    if not A.issuperset(read_int()):
        output.add(False)
        break
    else:
        output.add(True)
print(next(iter(output)))
def read_input():
    n = int(raw_input())
    return set(raw_input().split())

print(len(read_input().difference(read_input())))
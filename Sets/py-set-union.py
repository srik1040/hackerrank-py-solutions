def read_set():
    n = int(raw_input())
    return set(raw_input().split())

print(len(read_set().union(read_set())))
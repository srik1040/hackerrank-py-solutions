def read_input():
    n = int(input())
    return set(input().split())

print(len(read_input().symmetric_difference(read_input())))
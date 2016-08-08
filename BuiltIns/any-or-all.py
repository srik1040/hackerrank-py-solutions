N = int(raw_input())
d = map(int, raw_input().split())
print all([isinstance(i, int) and i > 0 for i in d]) and any([list(str(i)) == list(str(i))[::-1] for i in d])
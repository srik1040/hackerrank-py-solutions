#!/usr/bin/env python3

L = []
N = int(input())
for _ in range(N):
    command, *values = input().split()
    values = map(int, values)
    
    if command == 'print':
        print(L)
    else:
        getattr(L, command)(*values)
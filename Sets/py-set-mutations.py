n = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()[0]
    command_data = set(map(int, input().split()))

    getattr(A, command)(command_data)
    
print(sum(A))
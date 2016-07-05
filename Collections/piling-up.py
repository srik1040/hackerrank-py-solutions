# Enter your code here. Read input from STDIN. Print output to STDOUT
def validateCube(sideLengths):
    leftIndex = 0
    rightIndex = len(sideLengths) - 1
    prev_length = max(sideLengths[leftIndex], sideLengths[rightIndex])
    while leftIndex <= rightIndex:
        length = max(sideLengths[leftIndex], sideLengths[rightIndex])
        if length > prev_length:
            return False
        prev_length = length
        if sideLengths[leftIndex] == length:
            leftIndex += 1
        else:
            rightIndex -= 1
    return True

T = int(raw_input())
for _ in range(T):
    n = int(raw_input())
    sideLengths = list(map(int, raw_input().split()))
    print 'Yes' if validateCube(sideLengths) else 'No'
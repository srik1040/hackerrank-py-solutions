# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(raw_input())
for _ in range(T):
    try:
        re.compile(raw_input())
    except re.error:
        print False
    else:
        print True
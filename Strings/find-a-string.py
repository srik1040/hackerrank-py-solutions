# Enter your code here. Read input from STDIN. Print output to STDOUT
i_string = raw_input()
i_sub = raw_input()

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
print occurrences(i_string, i_sub)
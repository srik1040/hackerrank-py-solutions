# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
N = int(raw_input())
Student = collections.namedtuple('Student', raw_input().split())
marks = map(lambda student: float(student.MARKS), [Student._make(raw_input().split()) for _ in range(N)])
print "{0:.2f}".format(sum(marks) / len(marks))
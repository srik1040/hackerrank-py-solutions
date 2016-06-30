# Enter your code here. Read input from STDIN. Print output to STDOUT
import textwrap
i_str = raw_input()
i_width = int(raw_input())

for t in textwrap.wrap(i_str, i_width):
    print t
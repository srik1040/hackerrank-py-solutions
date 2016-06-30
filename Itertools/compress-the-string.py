# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
S = raw_input()

for i in itertools.starmap(lambda key, grp: (len(list(grp)), int(key)), itertools.groupby(S)):
    print i,
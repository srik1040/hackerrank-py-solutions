# Enter your code here. Read input from STDIN. Print output to STDOUT
input1 = int(raw_input())
i_data = []
score_data = []
name_data = []
for i in range(input1):
	name = raw_input()
	score = float(raw_input())
	i_data.append([name, score])
	score_data.append(score)

score_data = set(score_data)
score_data.remove(min(score_data))

name_data = [item[0] for item in i_data if item[1] == min(score_data)]
for item in sorted(name_data):
	print item
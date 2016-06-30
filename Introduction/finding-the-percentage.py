num_len = int(raw_input())
data_dict = {}
for i in range(num_len):
	input_item = raw_input()
	item_lst = input_item.split()
	data_dict[item_lst[0]] = item_lst[1:]

student_name = raw_input()
if student_name in data_dict:
	sum = 0
	for item in data_dict[student_name]:
		sum += float(item)
	print "{0:.2f}".format(sum / len(data_dict[student_name]) * 1.0)
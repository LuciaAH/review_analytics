# 留言分析
data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print (count / 1000000 * 100, '%')

data_sum = 0
for a in data:
	data_sum += len(a)
print ('每筆留言平均長度為', data_sum / len(data))
	
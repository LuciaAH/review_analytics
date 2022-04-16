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
	
# 文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print('請輸入_離開_結束查找。')
while True:
	word = input('請輸入欲查找之英文單字：')
	if word in wc:
		print(wc[word])
		continue
	elif word == '離開':
		break
	else:
		print('留言中無此單字唷!')
		continue




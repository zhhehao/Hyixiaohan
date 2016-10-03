import re

d = {}

# use re to filter word, use dict to static
with open('0004.txt', 'r') as f:
	for line in f.readlines():
		for word in line.split():
			if re.match(r'^[a-zA-Z]+$',word):
				if word.lower() in d:
					d[word.lower()] = d[word.lower()] + 1
				else:
					d[word.lower()] = 1

# put to list for sort
l = []
for k, v in d.items():
	l.append((k, v))

ls = sorted(l, key=lambda x: x[1], reverse=True)

# print top 10 records
for i in range(10):
	print('%s: %s' % (ls[i][0], ls[i][1]))

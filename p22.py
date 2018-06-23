
with open('p22.txt') as f:
	names = f.readline()

names = list(map(lambda n: n.strip('\"'), names.split(",")))
names.sort()

def score(s):
	total = 0
	for c in s:
		total += ord(c) - ord('A') + 1
	return total

total = 0
for i in range(len(names)):
	total += (i + 1) * score(names[i])

print(total)
	



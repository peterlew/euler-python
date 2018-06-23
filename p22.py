
with open('p22.txt') as f:
	names = f.readline()

names = list(map(lambda n: n.strip('\"'), names.split(",")))



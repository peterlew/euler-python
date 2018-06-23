
with open('p13.txt') as f:
	nums = f.readlines()

nums = list(map(lambda line: int(line.strip()), nums))

print(str(sum(nums))[:10])

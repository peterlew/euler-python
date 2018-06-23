
tot = 1
counter = 1

for i in range(1, 501):
	for j in range(4):
		counter += 2 * i
		tot += counter

print(tot)



fibs = [1]

curFib = 1
lastFib = 1

upperLimit = 4000000 

while curFib <= upperLimit:
	fibs.append(curFib)
	lastFib, curFib = curFib, lastFib + curFib

print(sum(filter(lambda n: n % 2 == 0, fibs)))

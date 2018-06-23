
coins = [200, 100, 50, 20, 10, 5, 2, 1]

# results dic: (target, max coin index) -> ways to make target
#				using coins at max index or greater
results = {}
for i in range(8):
	results[(0, i)] = 1

def waysToMake(n, ind):
	if (n, ind) in results:
		return results[(n, ind)]
	total = 0
	for i in range(ind, 8):
		coin = coins[i]
		if coin <= n:
			total += waysToMake(n - coin, i)
	results[(n, ind)] = total
	return total

print(waysToMake(200, 0))
		


	

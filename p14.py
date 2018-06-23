
results = {1 : 1}

def chainLen(n):
	if n in results:
		return(results[n])
	if n % 2 == 0:
		result = 1 + chainLen(n // 2)
	else:
		result = 1 + chainLen(n * 3 + 1)
	results[n] = result
	return result

longestChain = 0
longestChainStart = 0
for i in range(1, 1000000):
	c = chainLen(i)
	if c > longestChain:
		longestChain = c
		longestChainStart = i

print(longestChainStart)


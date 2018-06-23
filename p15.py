
results = {}

def numRoutes(w, h):
	if (w, h) in results:
		return results[(w, h)]
	if w == 0 or h == 0:
		results[(w, h)] = 1
		return( 1 )
	result = numRoutes(w - 1, h) + numRoutes(w, h - 1)
	results[(w, h)] = result
	return result

print(numRoutes(20, 20))

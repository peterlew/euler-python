
with open('p11.txt') as f:
	grid = f.readlines()

for i in range(0, 20):
	grid[i] = list(map(lambda x: int(x), grid[i].split()))

def prodVert(r, c):
	if r < 3:
		return(0)
	prod = 1
	for i in range(4):
		prod *= grid[r - i][c]
	return(prod)

def prodHor(r, c):
	if c < 3:
		return(0)
	prod = 1
	for i in range(4):
		prod *= grid[r][c - i]
	return(prod)

def prodDiagUp(r, c):
	if c > 16 or r < 3:
		return(0)
	prod = 1
	for i in range(4):
		prod *= grid[r - i][c + i]
	return(prod)

def prodDiagDown(r, c):
	if c > 16 or r > 16:
		return(0)
	prod = 1
	for i in range(4):
		prod *= grid[r + i][c + i]
	return(prod)

bestProd = 0
for r in range(20):
	for c in range(20):
		prod = max(prodVert(r, c), prodHor(r, c), prodDiagUp(r, c), prodDiagDown(r, c))
		bestProd = max(bestProd, prod)

print(bestProd)

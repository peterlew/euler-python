
with open('p18.txt') as f:
	tri = f.readlines()

#strip and separate numbers and cast as ints
tri = list(map(lambda line: list(map(lambda s: int(s), line.split())), tri))

maxFrom = {}

#fill results from last row as their face value
lastRowInd = len(tri) - 1
lastRow = tri[lastRowInd] 
for i in range(len(lastRow)):
	maxFrom[(lastRowInd, i)] = lastRow[i]

#work up the pyramid
for r in range(lastRowInd - 1, -1, -1):
	for c in range(len(tri[r])):
		faceValue = tri[r][c]
		leftRoute = maxFrom[(r + 1, c)]
		rightRoute = maxFrom[(r + 1, c + 1)]
		result = faceValue + max(leftRoute, rightRoute)
		maxFrom[(r, c)] = result

print(maxFrom[(0, 0)])



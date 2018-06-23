
numLetter = {
		0: 0, #for the math later, 0 will count for 0 letters
		1: 3,
		2: 3,
		3: 5,
		4: 4,
		5: 4,
		6: 3,
		7: 5,
		8: 5,
		9: 4,
		10: 3,
		11: 6,
		12: 6,
		13: 8,
		14: 8, 
		15: 7,
		16: 7,
		17: 9,
		18: 8,
		19: 8
	}

tenMults = {
		20: 6,
		30: 6,
		40: 5,
		50: 5,
		60: 5,
		70: 7,
		80: 6,
		90: 6
	}

for k, v in tenMults.items():
	for i in range(k, k + 10):
		numLetter[i] = v + numLetter[i - k]

for i in range(1, 10):
	numLetter[i * 100] = numLetter[i] + 7

for i in range(100, 1000, 100): 
	for j in range(i + 1, i + 100):
		numLetter[j] = numLetter[i] + 3 + numLetter[j - i]

numLetter[1000] = 11

print(sum(numLetter.values()))

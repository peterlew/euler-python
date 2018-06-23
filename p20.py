
from Useful import toDigits
from functools import reduce

print(sum(toDigits(reduce(lambda x, y: x * y, range(1, 101)))))


from matplotlib import pyplot

lwr = 19 * 10**9
upr = 21 * 10**9
stp = 100000

fDic = {}

def fOfN(d, n):
    mag = len(str(n))
    count = 0
    for i in xrange(0, mag):
        tx = 10**i
        ttx = 10 * tx
        count += tx * (n / ttx) + max(0, min((d + 1) * tx - 1, (n % ttx)) - (d * tx - 1))
    return count

data = {}
for i in xrange(1, 10):
    data[i] = []
    for j in range(lwr, upr, stp):
        data[i].append(fOfN(i, j))

colors = ['r-', 'b-', 'g-', 'c-', 'm-', 'y-', 'k-', 'b-', 'g-', 'c-', 'm-']

for i in xrange(1, 10):
    pyplot.plot(range(lwr, upr, stp), data[i], colors[i])
pyplot.plot(range(lwr, upr, stp), range(lwr, upr, stp), 'r-')
pyplot.xlim(lwr, upr)
pyplot.ylim(lwr, upr)
pyplot.show()
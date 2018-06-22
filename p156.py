
def fOfN(n):
    mag = len(str(n))
    count = 0
    for i in xrange(0, mag):
        tx = 10**i
        ttx = 10 * tx
        count += tx * (n / ttx) + max(0, min(2 * tx - 1, (n % ttx)) - (tx - 1))
    return count

def isHit(n):
    return n == fOfN(n)

def findHitLB(low, hi):
    avg = (low + hi) / 2
    fOfAvg = fOfN(avg)
    if fOfAvg == avg:
        return avg
    else:
        if fOfAvg < avg:
            return findHitLB(avg, hi)
        else:
            return findHitLB(low, avg)
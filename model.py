import sys
import numpy as np
import time
from Cache import Cache
from LRUCache import LRUCache
from FIFOCache import FIFOCache

import matplotlib.pyplot as plt


def rate(k):
    return 1 / (k + 1)


def combined_rate(n):
    return sum([1/(i+1) for i in range(n)])


def model(m: int, n: int, cache: Cache, T: int):
    start = time.time()
    total_rate = combined_rate(n)
    probability_list = [rate(i)/total_rate for i in range(n)]
    hit_ratio = [0]
    time_points = [0]
    for t in range(1, T + 1):
        next = np.random.choice(range(n), 1, probability_list)[0]
        cache.get(next)
        if t % 25 == 0:
            time_points.append(t)
            hit_ratio.append(cache.hits / (cache.hits + cache.misses))
            print("%.2f percent complete - %.2f seconds elapsed" % (round(t / T * 100, 3), round(time.time() - start, 3)), end='\r')
            sys.stdout.flush()
    print("")

    ax = plt.axes()
    ax.plot(time_points, hit_ratio)
    plt.savefig("graphs/{0}_{1}_{2}_{3}.png".format(m, n, T, cache.name))
    plt.show()


if __name__ == "__main__":
    m, n, T, cache = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    if cache == "LRU":
        model(m, n, LRUCache(m), T)
    elif cache == "FIFO":
        model(m, n, FIFOCache(m), T)
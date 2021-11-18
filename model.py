import sys
import time
from Cache import Cache
from LRUCache import LRUCache
from FIFOCache import FIFOCache
import random, math, bisect

import matplotlib.pyplot as plt


# Functions for sampling
def rate(k):
    return 1 / (k + 1)


def inverse_transform(k):
    l = rate(k)
    U = random.uniform(0, 1)
    return -math.log(U) / l


# Get a start time for all potential ks
def sample_start(n):
    timings = []
    for k in range(n):
        t = inverse_transform(k)
        timings.append((t, k))
    return sorted(timings, key=lambda x: x[0])


def plot_and_save(time_points, hit_ratio):
    # Plots the graph and saves it as a png
    ax = plt.axes()
    ax.plot(time_points, hit_ratio)
    plt.xlabel("Time (arbitrary units)")
    plt.ylabel("Hit-Ratio")
    plt.title("Hit Ratio Graph for an {0} Cache (m={1}, n={2})".format(cache.name, m, n))
    plt.savefig("graphs/{0}_{1}_{2}_{3}.png".format(m, n, T, cache.name))
    plt.show()


def model(n: int, cache: Cache, T: int):
    start = time.time()

    # Arrays for storing data that will be plotted
    hit_ratio = [0]
    time_points = [0]
    # Variable to keep track of current time in simulation
    t = 0

    # Variables for how often to take measurements of HR
    rate_of_data_collection = 1
    next_data_collected = rate_of_data_collection

    diary = sample_start(n)
    while t < T:
        # Get the next entry in the diary
        event = diary.pop(0)
        t = event[0]
        k = event[1]
        cache.get(k)
        tP = t + inverse_transform(k)
        bisect.insort(diary, (tP, k))

        # If enough time has passed, collect more graphing data
        if t // next_data_collected >= 1:
            time_points.append(t)
            hit_ratio.append(cache.hits / (cache.hits + cache.misses))
            next_data_collected += rate_of_data_collection
        
        # Print the progress, flushing out the previous print
        print("%.2f percent complete - %.2f seconds elapsed\t Current HR: %.4f" % (
            round(t / T * 100, 3), 
            round(time.time() - start, 3), 
            round(cache.hits / (cache.hits + cache.misses), 5)
        ), end='\r')
        sys.stdout.flush()
    
    print("")
    plot_and_save(time_points, hit_ratio)


if __name__ == "__main__":
    m, n, T, cacheStr = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    if cacheStr == "LRU":
        cache = LRUCache(m)
    elif cacheStr == "FIFO":
        cache = FIFOCache(m)
    else:
        Exception()

    model(n, cache, T)

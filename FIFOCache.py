from Cache import Cache

class FIFOCache(Cache):
    def __init__(self, capacity, starting_values=None):
        super().__init__(capacity, starting_values)

    def evict(self, value):
        self.cache = self.cache[1:] + [value]


if __name__ == "__main__":
    cache = FIFOCache(10, starting_values=[])
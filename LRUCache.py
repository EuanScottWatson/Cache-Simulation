from Cache import Cache

class LRUCache(Cache):
    def __init__(self, capacity, starting_values=None):
        super().__init__(capacity, starting_values)
        self.name = "LRU"

    def evict(self, value):
        self.cache = [value] + self.cache[:-1]

    def hit(self, value):
        index = self.cache.index(value)
        self.cache = [value] + self.cache[:index] + self.cache[index + 1:]


if __name__ == "__main__":
    cache = LRUCache(10, starting_values=[])
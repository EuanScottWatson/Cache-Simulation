class Cache:
    def __init__(self, capacity, starting_values=None):
        self.name = "Cache"
        self.capacity = capacity
        self.hits = 0
        self.misses = 0
        if starting_values:
            self.cache = starting_values + [-1 for _ in range(self.capacity - len(starting_values))]
        else:
            self.cache = [-1 for _ in range(self.capacity)]

    def evict(self, value):
        pass

    def hit(self, value):
        pass

    def get(self, value):
        if value in self.cache:
            self.hits += 1
            self.hit(value)
            return value
        else:
            self.misses += 1
            self.evict(value)

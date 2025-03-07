class RandomizedSet:

    def __init__(self):
        self.values = set()
    def insert(self, val: int) -> bool:
        if val not in self.values:
            self.values.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.values:
            self.values.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_element = random.choice(list(self.values))
        return random_element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
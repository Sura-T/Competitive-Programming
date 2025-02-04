class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.val = defaultdict(int)

    def add(self, number: int) -> None:
        prevFreq = self.freq[number]
        self.val[prevFreq] -= 1
        self.freq[number] += 1
        newFreq = self.freq[number]
        self.val[newFreq] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] != 0:
            prevFreq = self.freq[number]
            self.val[prevFreq] -= 1
            self.freq[number] -= 1
            newFreq = self.freq[number]
            self.val[newFreq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.val[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
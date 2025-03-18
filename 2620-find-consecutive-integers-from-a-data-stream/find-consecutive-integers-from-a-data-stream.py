class DataStream:

    def __init__(self, value: int, k: int):
        self.curr_val = value
        self.last_k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if num != self.curr_val:
            self.count = 0
        else:
            self.count += 1

        return self.count >= self.last_k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
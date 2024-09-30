class CustomStack:
    def __init__(self, max_size: int):
        self.stack = [0] * max_size
        self.add = [0] * max_size
        self.current_size = 0

    def push(self, x: int) -> None:
        if self.current_size < len(self.stack):
            self.stack[self.current_size] = x
            self.current_size += 1

    def pop(self) -> int:
        if self.current_size <= 0:
            return -1
        self.current_size -= 1
        result = self.stack[self.current_size] + self.add[self.current_size]
        if self.current_size > 0:
            self.add[self.current_size - 1] += self.add[self.current_size]
        self.add[self.current_size] = 0
        return result

    def increment(self, k: int, val: int) -> None:
        
        limit = min(k, self.current_size) - 1  
        if limit >= 0:
            self.add[limit] += val


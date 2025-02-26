class BrowserHistory:
    def __init__(self, homepage: str):
        self.backward_history = []
        self.forward_history = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.backward_history.append(url)
        self.forward_history.clear()

    def back(self, steps: int) -> str:
        while steps and len(self.backward_history) > 1:
            self.forward_history.append(self.backward_history.pop())
            steps -= 1
        return self.backward_history[-1]

    def forward(self, steps: int) -> str:
        while steps and self.forward_history:
            self.backward_history.append(self.forward_history.pop())
            steps -= 1
        return self.backward_history[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
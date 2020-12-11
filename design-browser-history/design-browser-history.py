class BrowserHistory:
​
    def __init__(self, homepage: str):
        self.arrList = [homepage]
        self.maxIdx = 0
        self.curIdx = 0
​
    def visit(self, url: str) -> None:
        if self.curIdx == len(self.arrList) - 1:
            self.arrList.append(url)
        else:
            self.arrList[self.curIdx + 1] = url
        self.curIdx += 1
        self.maxIdx = self.curIdx
        return self.arrList[self.curIdx]
​
    def back(self, steps: int) -> str:
        self.curIdx = 0 if self.curIdx < steps else self.curIdx - steps
        return self.arrList[self.curIdx]
​
    def forward(self, steps: int) -> str:
        self.curIdx = self.maxIdx if self.curIdx + steps > self.maxIdx else self.curIdx + steps
        return self.arrList[self.curIdx]
​
​
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

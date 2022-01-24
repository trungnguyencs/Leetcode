class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[0, set()] for _ in range(10)]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for t, s in self.arr:
            if timestamp - t < 10 and message in s:
                return False
        # clear memory 
        idx = timestamp % 10
        if self.arr[idx][0] == timestamp:
            self.arr[idx][1].add(message)
        else:
            self.arr[idx] = [timestamp, set([message])]
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
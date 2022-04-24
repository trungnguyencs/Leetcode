class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.stats = {}

    def checkIn(self, id: int, startStation: str, startTime: int) -> None:
        self.checkedIn[id] = [startStation, startTime]        

    def checkOut(self, id: int, endStation: str, endTime: int) -> None:
        startStation, startTime = self.checkedIn[id]
        if (startStation, endStation) not in self.stats:
            self.stats[(startStation, endStation)] = [0, 0]
        self.stats[(startStation, endStation)][0] += endTime - startTime
        self.stats[(startStation, endStation)][1] += 1
        del self.checkedIn[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stats[(startStation, endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
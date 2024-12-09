class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        ans = []
        dic = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            dic[name].append(time)
        for name, timeList in dic.items():
            if self.has3TimesInAnHour(timeList):
                ans.append(name)
        return sorted(ans)

    def has3TimesInAnHour(self, timeList):
        timeList.sort()
        for i in range(len(timeList) - 2):
            if self.convertToMinutes(timeList[i+2]) - self.convertToMinutes(timeList[i]) <= 60:
                return True
        return False
            
    def convertToMinutes(self, time):
        h, m = time.split(':')
        return 60*int(h) + int(m)
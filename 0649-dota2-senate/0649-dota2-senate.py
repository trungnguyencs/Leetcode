class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        banR = banD = 0
        countR = senate.count('R')
        countD = len(senate) - countR
        while countR and countD:
            cur = q.popleft()
            if cur == 'R':
                if banR > 0:
                    countR -= 1
                    banR -= 1
                else:
                    banD += 1
                    q.append('R')
            else:
                if banD > 0:
                    countD -= 1
                    banD -= 1
                else:
                    banR += 1
                    q.append('D')   
        return "Radiant" if countR else "Dire"
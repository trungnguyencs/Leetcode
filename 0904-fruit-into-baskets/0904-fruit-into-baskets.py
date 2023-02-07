class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        maxLen = l = 0
        for r, num in enumerate(fruits):
            dic[num] += 1
            
            while len(dic) > 2:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0: del dic[fruits[l]]
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #same as 159. Longest Substring with At Most Two Distinct Characters
        counter = Counter()
        l = maxWindow = 0
        for r, num in enumerate(fruits):
            counter[num] += 1
            while len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return maxWindow
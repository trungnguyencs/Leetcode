class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        arr.sort() # greedy: select high value items last
        maxVal = s = 0 # s is the sum of the numbers we have selected
        while arr:
            item = arr.pop()
            if s + item < 0: # if we add 1 new item then each item already selected will have their order increased by 1 -> val is increased by s
                break
            else:
                s += item
                maxVal += s 
        return maxVal
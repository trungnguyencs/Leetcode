class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correctOrder = sorted(heights)
        return len([i for i in range(len(heights)) if heights[i] != correctOrder[i]])
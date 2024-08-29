class Solution:
    def pathSum(self, nums: List[int]) -> int:
        G = defaultdict(int)
        ans = 0
        for num in nums:
            d = num//100
            p = (num//10) % 10
            v = num % 10
            # At each level, store the sum of all the previous nodes covered
            G[(d, p)] = v + G[(d - 1, (p + 1)//2)]
        # Sum up all values stored in all leaf nodes
        for d, p in G:
            if (d + 1, 2*p) not in G and (d + 1, 2*p - 1) not in G:
                ans += G[(d, p)]
        return ans
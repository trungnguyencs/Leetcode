class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dic = self.getDic(nums)
        ans = set()
        for s, list1 in dic.items():
            if target - s not in dic: continue
            list2 = dic[target - s]
            for a, b in list1:
                for c, d in list2:
                    if a not in [c, d] and b not in[c, d]:
                        ans.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
        return list(ans)
    
    def getDic(self, nums):
        dic = defaultdict(list)
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j:
                    dic[num1 + num2].append((i, j))
        return dic
        

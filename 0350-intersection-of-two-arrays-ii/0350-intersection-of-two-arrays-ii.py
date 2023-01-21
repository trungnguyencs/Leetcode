class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for num in nums1:
            if num not in dic: dic[num] = [0, 0]
            dic[num][0] += 1
        for num in nums2:
            if num not in dic: continue
            dic[num][1] += 1
        ans = []
        for num in dic:
            for _ in range(min(dic[num])):
                ans.append(num)
        return ans
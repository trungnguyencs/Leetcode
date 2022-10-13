# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        # using reservoir sampling
        # when seeing ith node:
        # probability to change to ith node is 1/i 
        # probability to keep current node is (i-1)/i
        # overall probability: 1/2*2/3*...*(k-1)/k = 1/k
        count = 1
        cur = randomNode = self.head
        while cur:
            if randint(1, count) == 1:
                randomNode = cur
            cur = cur.next
            count += 1
        return randomNode.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
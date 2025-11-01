# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur = prev.next
        m = defaultdict(int)
        for i in nums:
            m[i] = 1
        while cur:
            if m[cur.val]:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next
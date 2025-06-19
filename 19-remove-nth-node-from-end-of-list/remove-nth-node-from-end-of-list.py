# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        cur = head
        end = cur
        for _ in range(n-1):
            end = end.next
        while end.next:
            end = end.next
            prev = prev.next
            cur = cur.next
        prev.next = cur.next
        return dummy.next
        
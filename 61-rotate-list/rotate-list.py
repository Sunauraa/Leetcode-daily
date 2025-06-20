# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        count = 0
        dummy = head
        while dummy:
            count+=1
            dummy = dummy.next
        k%= count
        if not k:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        cur = prev.next
        end = cur
        for _ in range(k-1):
            end = end.next
        while end.next:
            end = end.next
            prev = prev.next
            cur = cur.next
        prev.next = None
        end.next = head
        head = cur
        return head
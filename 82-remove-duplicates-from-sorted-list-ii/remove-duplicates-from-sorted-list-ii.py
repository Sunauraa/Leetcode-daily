# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        cur = head
        while prev.next:
            cur = prev.next
            nx = cur.next
            if nx and cur.val == nx.val:
                while nx and cur.val == nx.val:
                    nx = nx.next
                prev.next = nx
            else:
                prev = prev.next
        return dummy.next


        
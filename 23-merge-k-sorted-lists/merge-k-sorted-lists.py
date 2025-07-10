# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        
        check = True
        while check:
            check = False
            mn = float('inf')
            for i in lists:
                if i:
                    mn = min(mn,i.val)
                    check = True
            for i in range(len(lists)):
                if lists[i] and lists[i].val == mn:
                    cur.next = lists[i]
                    lists[i] = lists[i].next
                    break
            if check:
                cur = cur.next
                cur.next = None
        return dummy.next

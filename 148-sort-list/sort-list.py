# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        #print(head.val)
        dummy = ListNode(0, head)
        fi = se = dummy
        while se and se.next:
            #print(se)
            se = se.next.next
            fi = fi.next
        sechalf = self.sortList(fi.next)
        fi.next = None
        firhalf = self.sortList(dummy.next)

        cur = root = ListNode(0, head)
        while firhalf != None and sechalf != None:
            if firhalf.val >= sechalf.val:
                cur.next = sechalf
                sechalf = sechalf.next
            else:
                cur.next = firhalf
                firhalf = firhalf.next
            cur = cur.next
        
        if firhalf != None:
            cur.next = firhalf
        if sechalf != None:
            cur.next = sechalf

        return root.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = ''
        while head:
            if head.val == 1:
                ans+='1'
            else:
                ans+='0'
            head = head.next
        res = 0
        n = len(ans)
        for i in range(len(ans)-1,-1,-1):
            if ans[i] == '1':
                res+=(1<<(n-i-1))
        return res
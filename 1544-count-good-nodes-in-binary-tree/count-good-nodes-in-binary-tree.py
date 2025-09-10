# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def bfs(root,mx):
            nonlocal res
            if not root:
                return
            if root.val >= mx:
                res+=1
            bfs(root.left,max(mx,root.val))
            bfs(root.right,max(mx,root.val))
        
        bfs(root,root.val)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dequy(root,depth):
            nonlocal ans
            if not root:
                return
            depth+=1
            ans = max(ans,depth)
            dequy(root.left,depth)
            dequy(root.right,depth)
        
        dequy(root,0)
        return ans

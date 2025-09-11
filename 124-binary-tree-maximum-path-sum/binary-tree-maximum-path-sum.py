# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            v = root.val
            left = dfs(root.left)
            right = dfs(root.right)

            #print(v,left,right)
            mx = max( left + v, right + v , v )
            res = max(res,mx, left + right + v)
            return mx
        
        dfs(root)
        return res
            
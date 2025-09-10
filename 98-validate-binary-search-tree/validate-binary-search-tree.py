# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs( root ):
            nonlocal res
            if not root:
                return inf,-inf
            
            mnl,mxl = dfs(root.left)
            mnr,mxr = dfs(root.right)
            print(root.val, mxl,mnr)
            if mxl >= root.val:
                res = False
            if mnr <= root.val:
                res = False

            return min(mnl,mnr,root.val), max(mxl,mxr,root.val) 
        
        dfs(root)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        cur = 0
        def segs(l,r):
            nonlocal cur
            if l > r:
                return None
            
            root = TreeNode(preorder[cur])
            mid = idx_map[ preorder[cur] ]
            cur+=1
            root.left = segs(l,mid-1)
            root.right = segs(mid + 1, r)
            return root

        res = segs(0,len(preorder)-1)
        return res
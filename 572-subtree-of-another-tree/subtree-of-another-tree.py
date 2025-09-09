# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            #print(q.val,p.val)
            if q.val != p.val:
                return False
            return check(q.left,p.left) and check(q.right,p.right)
        
        if not root:
            return False
        if check(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
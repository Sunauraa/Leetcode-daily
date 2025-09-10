# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = defaultdict(list)
        
        def dequy(root,depth):
            if not root:
                return
            m[depth].append(root.val)
            dequy(root.left,depth+1)
            dequy(root.right,depth+1)
        dequy(root,1)

        store = set( m.keys() )
        res =[]
        for i in store:
            res.append(m[i])

        return res
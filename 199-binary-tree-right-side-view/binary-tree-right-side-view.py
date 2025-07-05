# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs( node, height):
            if not node:
                return
            if not m[height+1]:
                ans.append(node.val)
            m[height+1] = 1
            bfs( node.right, height + 1)
            bfs( node.left, height + 1)
        ans = []
        m = defaultdict(int)
        bfs(root,0)
        return ans
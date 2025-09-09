# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = defaultdict(int)
        h = defaultdict(list)

        def dfs(root):
            if not root:
                return
            u = root.val
            v = root.left
            if v:
                v = v.val
                d[v] = d[u] + 1
                if not h[v]:
                    h[v] = [0]*22
                h[v][0] = u
                for i in range(1,20):
                    if d[v] >= (1<<i):
                        #print(h[v][i])
                        h[v][i] = h[ h[v][i-1] ][i-1]
                dfs(root.left)
            v = root.right
            if v:
                v = v.val
                if not h[v]:
                    h[v] = [0]*22
                h[v][0] = u
                d[v] = d[u]+1
                for i in range(1,20):
                    if d[v] >= (1<<i):
                        #print(h[v][i])
                        h[v][i] = h[ h[v][i-1] ][i-1]
                dfs(root.right)
        h[root.val] = [0]*22
        dfs(root)

        def lca( u,v ):
            if d[u] < d[v]:
                u,v = v,u
            if d[u] != d[v]:
                k = d[u] - d[v]
                for j in range(20):
                    if (1<<j)&k:
                        k-=(1<<j)
                        u = h[u][j]
            if u == v:
                return u
            #k = d[u]
            for j in range(20,-1,-1):
                if h[u][j] != h[v][j]:
                    u = h[u][j]
                    v = h[v][j]
            return h[u][0]

        key = lca(q.val,p.val)
        res = TreeNode(1)

        def find(root):
            nonlocal res
            if not root:
                return
            if root.val == key:
                res = root
                return
            find(root.left)
            find(root.right)

        find(root)
        return res
            

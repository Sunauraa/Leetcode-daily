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

        def dfs(root,par):
            if not root:
                return
            u = root.val
            h[u] = [-1]*22
            h[u][0] = par if par != -1 else -1
            d[u] = d[par] + 1 if par != -1 else 1
            for j in range(1,20):
                if h[u][j-1] != -1:
                    #print(u,h[u][j-1])
                    h[u][j] = h[ h[u][j-1]][j-1]
            dfs(root.left,u)
            dfs(root.right,u) 
            

        h[root.val] = [-1]*22
        dfs(root,-1)

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
            
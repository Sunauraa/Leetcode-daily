# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Initialize dictionaries
        depth = {}
        parent = {}  # parent[node.val] = parent node's val
        # For binary lifting
        up = {}  # up[node.val][i] = 2^i-th ancestor
        
        def dfs(node, par):
            if not node:
                return
                
            u = node.val
            depth[u] = depth[par.val] + 1 if par else 0
            parent[u] = par.val if par else -1
            
            # Initialize binary lifting table
            up[u] = {}
            up[u][0] = parent[u]
            
            # Fill binary lifting table
            for i in range(1, 20):
                if up[u][i-1] != -1 and up[u][i-1] in up:
                    up[u][i] = up[up[u][i-1]][i-1]
                else:
                    up[u][i] = -1
            
            # Recursively process children
            dfs(node.left, node)
            dfs(node.right, node)
        
        # Start DFS from root with no parent
        dfs(root, None)
        
        def get_lca(u_val, v_val):
            u, v = u_val, v_val
            
            # Bring both nodes to same depth
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Lift u up to depth of v
            k = depth[u] - depth[v]
            for i in range(20):
                if (k >> i) & 1:
                    u = up[u][i]
            
            if u == v:
                return u
                
            # Lift both nodes until their parents are the same
            for i in range(19, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            
            return up[u][0]
        
        # Find the node with the lca value
        lca_val = get_lca(p.val, q.val)
        
        # We need to return the actual TreeNode, not just the value
        # Let's do a BFS to find the node with lca_val
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.val == lca_val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
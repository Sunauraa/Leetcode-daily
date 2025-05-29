class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        even2 = [0]*m
        leneven2 = self.dfs( 0 , -1 , 0 , graph2, even2 )

        even1  = [0]*n
        leneven1 = self.dfs( 0 , -1 , 0 , graph1 , even1 )

        b = max( sum(even2) , m - sum(even2) )
        a = sum(even1)
        ans = []
        for i in range(n):
            if even1[i]:
                ans.append( b + a )
            else:
                ans.append( b + n - a )
        return ans

    def dfs( self, u , p , dis , graph , even ):
        even[u] = dis%2
        for v in graph[u]:
            if v != p:
                self.dfs(v, u , dis + 1, graph , even)





        
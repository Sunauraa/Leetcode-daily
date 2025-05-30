class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges) + 1
        visit1 = self.dfs( node1 , [-1]*n , 0 , edges )
        visit2 = self.dfs( node2 , [-1]*n  , 0 , edges )
        curdis = 1000000
        ans = -1
        for i in range( n ):
            if visit1[i] != -1 and visit2[i] != -1:
                if curdis > max( visit1[i] , visit2[i] ):
                    curdis = max( visit1[i] , visit2[i] )
                    ans = i
        return ans
    def dfs( self, node, visit, dis, graph ):
        if visit[node] != -1:
            return [-1]*len(visit)
        visit[node] = dis
        if graph[node] != -1:
            self.dfs( graph[node] , visit , dis + 1 , graph )
        return visit
                

        
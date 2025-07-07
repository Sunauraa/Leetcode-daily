class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[1])
        parent = [ i for i in range(events[-1][1]+2) ]

        def findparent( u ):
            if parent[u] == u:
                return u
            parent[u] = findparent(parent[u])
            return parent[u]

        res = 0
        for i in events:
            time = findparent(i[0])
            if time <= i[1]:
                res+=1
                parent[time] = time+1

        return res
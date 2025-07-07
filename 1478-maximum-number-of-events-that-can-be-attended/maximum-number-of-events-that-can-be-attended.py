class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        parent = [ i for i in range(10**5+2) ]
        events.sort(key = lambda x: x[1])
        #print(events)

        def findparent( u ):
            if parent[u] == u:
                return u
            parent[u] = findparent(parent[u])
            return parent[u]
        
        def union(a,b):
            a = findparent(a)
            b = findparent(b)
            if a > b: a,b = b,a
            parent[a] = b

        res = 0
        for i in events:
            time = findparent(i[0])
            if time <= i[1]:
                res+=1
                parent[time] = time+1

        return res
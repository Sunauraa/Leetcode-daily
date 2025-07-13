class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #print(len(profits))
        m = defaultdict(list)
        for u,v in zip(profits, capital):
            m[v].append(u)

        q = []
        cur = 0
        key = sorted(list(m.keys()))
        while k > 0:
            #print(q)
            #print(len(key),cur,key[cur])
            while cur < len(key) and key[cur] <= w:
                #print(2)
                for x in m[key[cur]]:
                    heapq.heappush(q, -x)
                cur +=1
            if q:
                #print(1)
                temp = heapq.heappop(q)
                #print(temp)
                w -= temp
            #print(w)
            k-=1
        return w
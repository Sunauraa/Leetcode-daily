class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        m = defaultdict(list)
        for u,v in zip(profits, capital):
            m[v].append(u)

        q = []
        cur = 0
        key = sorted(list(m.keys()))
        while k > 0:
            while cur < len(key) and key[cur] <= w:
                for x in m[key[cur]]:
                    heapq.heappush(q, -x)
                cur +=1
            if q:
                temp = heapq.heappop(q)
                w -= temp
            k-=1
        return w
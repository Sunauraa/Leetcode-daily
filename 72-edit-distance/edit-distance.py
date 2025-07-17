class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        q = []
        heapq.heapify(q)
        ans = float('inf')
        store = set()
        heapq.heappush(q, (0,word1,word2))
        while q:
            step,x,y = heapq.heappop(q)
            if ans < step:
                return ans
            if (x,y) in store:
                continue
            store.add((x,y))
            while x and y and x[0] == y[0]:
                x = x[1:]
                y = y[1:]
            if x == y:
                ans = min(ans,step)
            elif not x:
                ans = min(ans,step + len(y))
            elif not y:
                ans = min(ans, step + len(x))
            else:
                heapq.heappush(q,(step+1, x[1:], y[1:]  ))
                heapq.heappush(q,(step+1, x[1:], y))
                heapq.heappush(q,(step+1, x,y[1:]))
        return ans
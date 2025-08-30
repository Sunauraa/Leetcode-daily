class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            while q and q[0][0] < temperatures[i]:
                res[q[0][1]] = i - q[0][1]
                heapq.heappop(q)
            heapq.heappush(q, (temperatures[i],i) )
        return res

        
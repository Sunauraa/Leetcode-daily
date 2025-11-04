class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n-k+1):
            c = Counter(nums[i:i+k])
            heap = [(-freq,-val) for val,freq in c.items()]
            heapq.heapify(heap)
            s=0
            for _ in range(min(x,len(heap))):
                freq,val = heapq.heappop(heap)
                s+=(-freq)*(-val)
            res.append(s)
        return res
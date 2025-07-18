class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = len(nums)//3
        left = [0]*m
        prefSum = 0
        maxheap = []
        for i in range(n):
            prefSum += nums[i]
            left[i] = prefSum
            heapq.heappush(maxheap,-nums[i])
        for i in range(n,n*2):
            heapq.heappush(maxheap,-nums[i])
            val = -heappop(maxheap)
            left[i] = left[i-1]
            left[i] += nums[i] - val
        
        right = [0]*m
        prefSum = 0
        minheap = []
        for i in range(m-1,n*2-1, -1):
            prefSum += nums[i]
            right[i] = prefSum
            heapq.heappush(minheap, nums[i])
        for i in range(n*2-1, n-1,-1):
            heapq.heappush(minheap, nums[i])
            val = heapq.heappop(minheap)
            right[i] = right[i+1]
            right[i] += nums[i] - val

        res = float('inf')
        for i in range(n-1,n*2):
            res = min(res, left[i] - right[i+1])
        return res
        
        
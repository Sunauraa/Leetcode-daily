class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = -inf
        cnt = 0
        for i in nums:
            prev = cur
            #print(cur)
            if i > cur:
                cur = max(i-k,cur+1)
                cnt+=1
            else:
                cur = min(i+k,cur+1)
                cnt+=1
            if cur == prev:
                cnt-=1
            #print(cur)
        return cnt
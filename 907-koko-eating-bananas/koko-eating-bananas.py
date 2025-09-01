class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            time = 0
            for pile in piles:
                time += pile//k + (pile%k > 0)
            return time <= h
        
        l, r = 1, 10**9
        ans = 10**9
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1

        return ans
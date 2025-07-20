class Solution:
    def twoEggDrop(self, n: int) -> int:
        ans = float('inf')
        l = 0
        r = n
        while l <= r:
            mid  = (l+r)//2
            if mid*(mid+1)//2 < n:
                ans = min(ans,(mid+n - (mid*(mid+1)//2)))
                l = mid + 1
            else:
                ans = min(ans,mid)
                r = mid - 1
        return ans
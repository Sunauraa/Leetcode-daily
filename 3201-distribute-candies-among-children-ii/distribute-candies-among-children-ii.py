class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        r = n - limit
        l = 0
        for i in range( 0 , limit + 1 ):
            l = i + limit
            if l > n:
                l = n
            if r < i:
                r = i
            if l >= r:
                ans += l - r + 1
        return ans
                
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if self.check(mid,citations,n):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
    def check(self , x , citations, n):
        count = 0
        for i in citations:
            if i >= x:
                count+=1
        if count >= x:
            return True
        return False
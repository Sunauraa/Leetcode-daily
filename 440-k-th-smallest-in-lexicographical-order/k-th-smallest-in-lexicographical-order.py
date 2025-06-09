class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k-=1
        while k > 0:
            steps = self.countSteps(n, curr, curr + 1)
            if steps <= k:
                curr+=1
                k-=steps
            else:
                curr*=10
                k-=1
        return curr
    
    def countSteps( self, n , curr, next):
        steps = 0
        while curr <= n:
            steps += min( n + 1 , next) - curr
            curr*=10
            next*=10
        return steps
        
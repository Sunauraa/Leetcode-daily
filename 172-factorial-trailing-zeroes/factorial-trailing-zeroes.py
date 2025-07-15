class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt2 = 0
        cnt5 = 0
        for i in range(1,n+1):
            while not i%2:
                cnt2+=1
                i//=2
            while not i%5:
                cnt5+=1
                i//=5
        return min(cnt2,cnt5)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if (1<<i)&num:
                    sum+=1
            sum%=3
            ans = ans|(sum<<i)
        
        if ans >= 2**31:
            ans-=2**32
        return ans

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p,q = 0,0
        n = len(nums)
        ans = False
        for p in range(1,n):
            for q in range(p + 1,n-1):
                #print(p,q)
                lose = False
                for i in range(1,p + 1):
                    if nums[i] <= nums[i-1]:
                        lose = True
                        break
                for i in range(p + 1,q + 1):
                    if nums[i] >= nums[i-1]:
                        lose = True
                        break
                for i in range(q + 1,n):
                    if nums[i] <= nums[i-1]:
                        lose = True
                        break
                if not lose:
                    #rint(p,q)
                    ans = True
        return ans
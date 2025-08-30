class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        total = 1
        for i in nums:
            total*=i
            left.append(total)
        n = len(nums)
        right = [0]*n
        total = 1
        for i in range(n-1,-1,-1):
            total*=nums[i]
            right[i] = total
        res = []
        #print(left)
        #print(right)
        for i in range(n):
            if i == 0:
                res.append(right[i+1])
            elif i == n -1:
                res.append(left[i-1])
            else:
                res.append(left[i-1]*right[i+1])
        return res
        
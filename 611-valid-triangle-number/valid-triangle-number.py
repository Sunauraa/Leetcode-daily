class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = SortedList(nums)
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                #print(nums[i] + nums[j])
                pos = nums.bisect_left(nums[i]+nums[j])
                #print(pos)
                #print()
                ans+= max(0,pos - j -1)
        return ans

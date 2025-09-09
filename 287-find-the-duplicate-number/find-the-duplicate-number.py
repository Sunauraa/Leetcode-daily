class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num == nums[num-1]:
                if i == num-1:
                    i+=1
                    continue
                else:
                    return num
            else:
                nums[num-1],nums[i] = nums[i],nums[num-1]
                i-=1
            i+=1
            
                
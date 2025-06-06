class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        i = 0
        temp = 0
        curlen = 10**5+2
        n = len(nums)
        while i < n:
            while j < n and temp < target:
                temp += nums[j]
                j+=1
            if curlen > j - i and temp >= target:
                curlen = j - i
            temp -= nums[i]
            i+=1
        return curlen*(curlen!= 10**5+2)

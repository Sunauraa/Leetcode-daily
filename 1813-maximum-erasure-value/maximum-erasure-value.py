class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum = 0
        m = defaultdict(int)
        back = 0
        ans = 0
        for i in nums:
            m[i]+=1
            sum += i
            while m[i] > 1:
                sum-=nums[back]
                m[nums[back]]-=1
                back+=1
            ans = max(ans,sum)
        return ans
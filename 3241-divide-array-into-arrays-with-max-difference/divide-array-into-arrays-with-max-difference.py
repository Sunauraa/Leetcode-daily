class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        step = 3
        for i in range( 0 , n , step ):
            if nums[i+step-1] - nums[i] > k:
                return []
            else:
                ans.append(nums[i:i+step])
        return ans
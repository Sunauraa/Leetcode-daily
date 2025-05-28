class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        arr = [0]*n
        for i in range(len(queries)):
            arr[ queries[i][0] ] -=1
            k = queries[i][1]
            if k < n - 1:
                arr[ k + 1 ]+=1
        for i in range(n):
            if i:
                arr[i] += arr[i-1]
            if nums[i] + arr[i] > 0:
                return False
        return True
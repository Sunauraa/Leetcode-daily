class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            #print(l,r)
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] < nums[0]:
                    r = mid - 1
                elif target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] >= nums[0]:
                    l = mid + 1
                elif target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
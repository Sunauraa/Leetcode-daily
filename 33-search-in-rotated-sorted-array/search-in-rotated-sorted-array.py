class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= nums[0]:
                if nums[mid] > target:
                    if target < nums[0]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if target < nums[0]:
                        l = mid + 1
                    else:
                        r = mid - 1
            print(l,r)
        if nums[l%len(nums)] == target:
            return l%len(nums)
        if nums[r%len(nums)] == target:
            return r%len(nums)
        return -1

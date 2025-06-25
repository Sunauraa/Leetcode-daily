class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs(target):
            count = 0
            negcount = sum(1 for x in nums1 if x < 0)

            start = negcount - 1 if target >= 0 else 0
            end = -1 if target >= 0 else negcount
            step = -1 if target >= 0 else 1
            left = 0

            for i in range(start, end,step):
                while left < len(nums2) and nums1[i]*nums2[left] > target:
                    left+=1
                count += len(nums2) - left
            start = negcount if target >= 0 else len(nums1) - 1
            end = len(nums1) if target >= 0 else negcount - 1
            step = 1 if target >= 0 else -1
            right = len(nums2) - 1

            for i in range(start, end, step):
                if nums1[i] == 0:
                    if target >= 0:
                        count += len(nums2)
                    continue
                while right >= 0 and nums1[i]*nums2[right] > target:
                    right-=1
                count += right + 1
            return count
        left, right = -10**10,10**10
        while left <= right:
            mid = (left + right)//2
            if count_pairs(mid) >= k:
                right = mid-1
            else:
                left = mid + 1
        return left


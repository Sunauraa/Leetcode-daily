class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        n,m = len(nums1), len(nums2)
        l,r = 0,n
        while l <= r:
            mid1 = (l+r)//2
            mid2 = (m+n+1)//2 - mid1

            max1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            max2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
            min1 = float('inf') if mid1 == n else nums1[mid1]
            min2 = float('inf') if mid2 == m else nums2[mid2]

            if max1 <= min2 and max2 <= min1:
                if (m+n)%2 == 0:
                    return (max(max1,max2)+ min(min1,min2))/2
                else:
                    return max(max1,max2)
            elif max1 > min2:
                r = mid1 - 1
            else:
                l = mid1 + 1
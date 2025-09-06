class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        n,m = len(nums1),len(nums2)
        l, r = 0, n
        while l <= r :
            mid1 = (l+r)//2
            mid2 = (n+m+1)//2 - mid1

            #print(mid1,mid2)
            max1 = float('-inf') if not mid1 else nums1[mid1-1]
            max2 = float('-inf') if not mid2 else nums2[mid2-1]
            min1 = float('inf') if mid1 == n else nums1[mid1]
            min2 = float('inf') if mid2 == m else nums2[mid2]

            #print(min1,max1,min2,max2)
            #print()
            if min1 >= max2 and min2 >= max1:
                if (n+m)%2:
                    return 1.0*max(max1,max2)
                else:
                    return (min(min2,min1) + max(max1,max2))/2

            if max1 > max2:
                r = mid1 - 1
            else:
                l = mid1 + 1
        print('wowow')
            
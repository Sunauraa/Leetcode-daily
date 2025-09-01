class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        m = defaultdict(int)
        for i,num in enumerate(nums2):
            m[num] = i
        
        #value se la vi tri cua num2, trong khi idx se la vi tri cua num1
        indices = [ m[num] for num in nums1 ]

        #print(indices)
        left = []
        arr = SortedList()
        for idx in indices:
            left.append(arr.bisect_left(idx))
            arr.add(idx)
        
        n = len(nums1)
        right = [0]*n
        arr = SortedList()
        for idx in range(n-1,-1,-1):
            #print(arr,indices[idx])
            right[idx] = len(arr) - arr.bisect_left( indices[idx] )
            arr.add(indices[idx])

        #print(left)
        #print(right)
        return sum( l*r for l,r in zip(left,right)  )
        
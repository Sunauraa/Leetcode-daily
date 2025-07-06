class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = defaultdict(int)
        for i in nums2:
            self.m[i]+=1

    def add(self, index: int, val: int) -> None:
        self.m[self.nums2[index]]-=1
        self.nums2[index] += val
        self.m[self.nums2[index]]+=1

    def count(self, tot: int) -> int:
        res = 0
        m = self.m
        nums1 = self.nums1
        for i in nums1:
            if tot > i:
                res += m[tot - i]
        if res == 26:
            print(m,nums1)
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
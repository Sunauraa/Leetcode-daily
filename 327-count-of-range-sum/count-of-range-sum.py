class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        arr = SortedList([0])
        pref = [0]
        ans = 0
        for i in nums:
            pref.append(pref[-1]+i)
            l = arr.bisect_right(pref[-1] - lower)
            r = arr.bisect_left(pref[-1] - upper )
            arr.add(pref[-1])
            #print(l,r)
            ans+= l - r
        return ans
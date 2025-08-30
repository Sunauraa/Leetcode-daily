class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = Counter(nums)
        res = SortedList( [ (count,key) for key,count in arr.items() ] )
        #print(res)
        return [ x for _,x in res[len(res)-k:] ]
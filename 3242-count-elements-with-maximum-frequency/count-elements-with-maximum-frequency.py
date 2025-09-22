class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i in nums:
            m[i]+=1
        mx = list(m.values())
        return mx.count( max(mx) )*max(mx)
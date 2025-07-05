class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = defaultdict(int)
        for i in arr:
            m[i]+=1
        for i in sorted(list(m.keys()), reverse = True):
            if i == m[i]:
                return i
        return -1
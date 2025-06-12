class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cur = 0
        m = defaultdict(int)
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in m:
                cur+=1
                m[temp] = cur
        ans = [ [] for i in range(cur) ]
        for i in strs:
            temp = ''.join(sorted(i))
            ans[m[temp]-1].append(i)
        return ans
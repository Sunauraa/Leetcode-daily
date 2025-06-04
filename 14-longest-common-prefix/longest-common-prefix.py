class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0:
            return ''
        if n == 1:
            return strs[0]
        for i in range( len(strs[0]) , -1 , -1 ):
            temp = strs[0][:i]
            check = 1
            for j in strs:
                if i > len(j) or temp not in j[:i]:
                    check = 0
                    break
            if check:
                return temp
        return ''
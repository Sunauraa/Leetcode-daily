class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        check = 0
        lib = dict()
        for i in words:
            if i in lib:
                lib[i]+=1
            else:
                lib[i] = 1
        check = 0
        for i in lib.keys():
            k = i[::-1]
            if k in lib:
                if i[0] == i[1]:
                    while lib[i] >= 2:
                        ans+=4
                        lib[i]-=2
                    if lib[i] == 1 and not check:
                        check = 1
                        ans+=2
                        lib[i]-=1
                else:
                    while lib[i] >= 1 and lib[k] >= 1:
                        ans+=4
                        lib[i]-=1
                        lib[k]-=1
        return ans
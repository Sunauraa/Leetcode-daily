class Solution:
    def numSteps(self, s: str) -> int:
        s = "0" + s
        s = list(s)
        n = len(s)
        ans = 0
        while s[n-1] != "1" or s.count("1") != 1:
            #print(s)
            if s[n-1] == '1':
                check = True
                fi = n-1
                while check:
                    if s[fi] == '1':
                        s[fi] = "0"
                    else:
                        s[fi] = '1'
                        check = False
                    fi-=1
            else:
                for i in range(n-1,0,-1):
                    if s[i-1] == '1':
                        s[i-1] = '0'
                        s[i] = '1' 

            ans+=1
        return ans

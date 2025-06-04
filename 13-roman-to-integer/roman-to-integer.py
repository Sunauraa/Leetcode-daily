class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        m=dict()
        m['I'] = 1
        m['V'] = 5
        m['X'] = 10
        m['L'] = 50
        m['C'] = 100
        m['D'] = 500
        m['M'] = 1000
        while i < n:
            if s[i] == 'I':
                if i < n - 1:
                    if s[i+1] != 'V' and s[i+1] != 'X':
                        ans += 1
                    elif s[i+1] == 'V':
                        ans+=4
                        i+=1
                    else:
                        ans+=9
                        i+=1
                else:
                    ans+=1
            elif s[i] == 'X':
                if i < n - 1:
                    if s[i+1] != 'L' and s[i+1] != 'C':
                        ans += 10
                    elif s[i+1] == 'L':
                        ans+=40
                        i+=1
                    else:
                        ans+=90
                        i+=1
                else:
                    ans+=10
            elif s[i] == 'C':
                if i < n - 1:
                    if s[i+1] != 'D' and s[i+1] != 'M':
                        ans += 100
                    elif s[i+1] == 'D':
                        ans+=400
                        i+=1
                    else:
                        ans+=900
                        i+=1
                else:
                    ans+=100
            else:
                ans+=m[s[i]]
            i+=1
        return ans

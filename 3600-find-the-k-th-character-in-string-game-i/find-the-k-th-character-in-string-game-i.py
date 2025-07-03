class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 'a'
        while len(ans) < k:
            temp = ''
            for i in ans:
                if i != 'z':
                    temp+=chr(ord(i)+1)
                else:
                    temp+='a'
            ans+=temp
        return ans[k-1]
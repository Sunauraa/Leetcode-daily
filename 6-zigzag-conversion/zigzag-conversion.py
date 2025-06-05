class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or n <= numRows :
            return s
        steps = numRows*2 - 2
        ans = ''
        for i in range(numRows):
            ans += s[i]
            for j in range( i + steps , n + 2000 , steps ):
                if i != 0 and i != numRows-1 and j != i and j - 2*i < n:
                    ans += s[j-2*i]
                if j < n:
                    ans += s[j]
                else:
                    break
        return ans

        
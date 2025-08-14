class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cur = '0'
        res = ''
        for i in range(2,len(num)):
            if num[i] == num[i-1] and num[i-1] == num[i-2] and cur <= num[i]:
                cur = num[i]
                res = cur*3
        return res
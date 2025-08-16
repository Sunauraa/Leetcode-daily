class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        res = ''
        check = True
        for i in num:
            if check and i == '6':
                res+='9'
                check = False
            else:
                res+=i
        return int(res)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        check = False
        for i in range(31,-1,-1):
            if left&(1<<i) or right&(1<<i):
                check = True
            if left&(1<<i) and right&(1<<i):
                ans|=(1<<i)
            elif left&(1<<i) == right&(1<<i):
                continue
            elif check:
                return ans
        return ans
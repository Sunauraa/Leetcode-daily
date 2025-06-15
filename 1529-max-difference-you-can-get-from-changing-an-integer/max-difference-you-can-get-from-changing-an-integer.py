class Solution:
    def maxDiff(self, num: int) -> int:
        nums = str(num)
        mx = nums
        for i in nums:
            if i != '9':
                mx = nums.replace(i, '9')
                break
        mn = nums
        if mn[0] != '1':
            mn = mn.replace(mn[0], '1')
        else:
            for i in range(1,len(mn)):
                if mn[i] != '0' and mn[i] != mn[0]:
                    mn = mn.replace(mn[i],'0')
                    break
        return int(mx) - int(mn)
        
        
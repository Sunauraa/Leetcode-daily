class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = str(num)
        mx = nums
        for i in nums:
            if i != '9':
                mx = nums.replace(i, '9')
                break
        mn = nums
        for i in nums:
            if i != '0':
                mn = nums.replace(i,'0')
                break
        return int(mx) - int(mn)
        
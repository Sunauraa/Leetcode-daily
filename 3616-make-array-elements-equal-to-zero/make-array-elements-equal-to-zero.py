class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0]*n
        r = [0]*n
        for i in range(n):
            if i == 0:
                l[i] = nums[i]
            else:
                l[i]+=nums[i] + l[i-1]
        for i in range(n-1,-1,-1):
            if i == n-1:
                r[i] = nums[i]
            else:
                r[i]+=nums[i] + r[i+1]
        
        cnt = 0
        for i in range(n):
            if not nums[i]:
                if l[i] == r[i]:
                    cnt+=2
                elif l[i] == r[i] + 1:
                    cnt+=1
                elif l[i] + 1 == r[i]:
                    cnt+=1
        return cnt
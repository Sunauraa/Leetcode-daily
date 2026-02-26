class Solution:
    def newr(self,pos,nums: List[int]):
        n = len(nums)
        i = pos
        if i >= n-2:
            return 0,0,0,0
        while i < n - 2 and nums[i] > nums[i-1]:
            i+=1
        p = i - 1
        print('Ly:',i,p,pos,n)
        if nums[i] == nums[i-1] or p < pos :
            l = i
            return self.newr(i + 1,nums)
        while i < n and nums[i] < nums[i-1]:
            i+=1
        q = i-1
        print('Hong:',i,q,pos,n)
        if i == n:
            return 0,0,0,0
        if nums[i] == nums[i-1]:
            l = i
            return self.newr(i + 1,nums)
        fi = True
        sm = 0
        mx = -inf
        r = i
        while i < n and nums[i] > nums[i-1]:
            sm+=nums[i]
            if mx < sm:
                r = i
                mx = sm
            i+=1
        print('An:',p,q,r)
        return pos-1,p,q,r

    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]*n
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        l = 0
        l,p,q,r = self.newr(1,nums)
        ans = -inf
        while l < n-3:
            if not (l<p<q<r):
                if ans == -inf:
                    return 0
                else:
                    return ans
            print('xinh dep:',l,p,q,r)
            for i in range(l,p):
                if i == 0:
                    ans = max(ans,prefix[r])
                else:
                    ans = max(ans,prefix[r] - prefix[i-1])
            l = q
            l,p,q,r = self.newr(l + 1,nums)
        return ans
        
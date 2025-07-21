class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(0):
            ans = [0]
            i = 0
            for j in range(n):
                if nums[j] == 0 and i != j:
                    ans.append(self.maxProduct(nums[i:j]))
                if nums[j] == 0:
                    i = j + 1
            if i != n:
                ans.append(self.maxProduct(nums[i:n]))

            print(ans)
            return max(ans)
        else:
            neg = sum( 1 for i in nums if i < 0  )
            if not neg or not neg%2 or n == 1:
                return prod(nums)
            i = 0
            j = n-1
            ans1 = 1
            ans2 = 1
            c = neg
            check1 = False
            for i in nums:
                if i < 0:
                    c -=1
                if i < 0 and not c:
                    break
                ans1*=i
                check1 = True
            c = neg
            check2 = False
            for i in range(n-1,-1,-1):
                if nums[i] < 0:
                    c-=1
                if nums[i] < 0 and not c:
                    break
                ans2*=nums[i]
                check2 = True
            #print(ans1,ans2,check1,check2)
            return max(ans1*check1,ans2*check2)
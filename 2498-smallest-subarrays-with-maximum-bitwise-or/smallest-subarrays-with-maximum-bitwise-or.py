class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mx = [0]*n
        for i in range(n-1,-1,-1):
            if i == n-1:
                mx[i] = nums[i]
            else:
                mx[i] = nums[i]|mx[i+1]
        store = [0]*31
        def add(x):
            nonlocal cur
            for i in range(30,-1,-1):
                if x >= (1<<i):
                    store[i]+=1
                    x-=(1<<i)
                    if store[i] == 1:
                        cur+=(1<<i)

        def remove(x):
            nonlocal cur
            for i in range(30,-1,-1):
                if x >= (1<<i):
                    store[i]-=1
                    x-=(1<<i)
                    if store[i] == 0:
                        cur-=(1<<i)

        r = 0
        ans = []
        cur = 0
        for l in range(n):
            while r < n and cur != mx[l]:
                #print(r,cur)
                add(nums[r])
                #print(cur)
                #print()
                r+=1
            if cur == 0:
                ans.append(1)
            else: ans.append(r-l)
            remove(nums[l])
        return ans
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans = set()
        j = 0
        n = len(nums)
        for i in range(n):
            j = i
            count = 0
            temp = ''
            while j < n and count <= k:
                if not nums[j]%p:
                    count +=1
                temp += chr(nums[j])
                j+=1
                if count <= k:
                        ans.add(temp)
        return len(ans)
        
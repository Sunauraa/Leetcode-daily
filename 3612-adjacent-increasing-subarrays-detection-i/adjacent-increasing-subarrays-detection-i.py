class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cnt = 0
        cur = -inf
        tot = 0
        for num in nums:
            if cur < num:
                cnt+=1
                cur = num
                if (cnt == k and tot) or cnt == k*2:
                    return True
            else:
                if tot == 1:
                    if cnt >= k:
                        return True
                    tot = 0
                elif cnt >= k:
                    tot = 1
                else:
                    tot = 0
                cnt = 1
                cur = num
        if tot and cnt >= k:
            return True
        return False
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]

        for num in nums[1:]:
            i = bisect.bisect_left(seq, num)

            if i == len(seq):
                seq.append(num)
            else:
                seq[i] = num
        
        return len(seq)
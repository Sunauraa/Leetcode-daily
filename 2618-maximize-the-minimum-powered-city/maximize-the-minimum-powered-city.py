class Solution:
    def maxPower(self, nums: List[int], r: int, k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        power = [0] * n
        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            power[i] = pre[right + 1] - pre[left]

        def ok(x):
            diff = [0] * (n + 1)
            add = 0
            rem = k
            for i in range(n):
                add += diff[i]
                curr = power[i] + add
                if curr < x:
                    need = x - curr
                    if rem < need:
                        return False
                    rem -= need
                    add += need
                    end = i + 2 * r + 1
                    if end < n:
                        diff[end] -= need
            return True

        low, high = 0, max(power) + k
        while low < high:
            mid = (low + high + 1) // 2
            if ok(mid):
                low = mid
            else:
                high = mid - 1
        return low
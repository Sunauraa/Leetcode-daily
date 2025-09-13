class Solution:
    def maxFreqSum(self, s: str) -> int:
        return max( [ s.count(x) for x in 'aeuoi' ] ) + max( [s.count(x) for x in 'qwrtypsdfghjklzxcvbnm'] )
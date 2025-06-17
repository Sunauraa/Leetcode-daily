class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod, d = 10**9+7, n-1
        if k > d:
            return 0
        r = min(k,d-k)
        c = 1
        if r:
            inv = [0]*(r+1)
            inv[1] = 1
            for i in range(2, r+1):
                inv[i] = mod - (mod//i)*inv[mod%i]%mod
            for i in range(1,r+1):
                c = c*(d-r+i)%mod*inv[i]%mod
        return m*c%mod*pow(m-1,d-k,mod)%mod
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        for u,v in zip_longest(ver1,ver2,fillvalue = 0):
            u,v = int(u),int(v)
            if u > v:
                return 1
            elif v > u:
                return -1
        return 0
            
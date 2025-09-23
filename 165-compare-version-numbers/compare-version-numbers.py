class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        dif = abs(len(ver1) - len(ver2))
        #print(dif,len(ver1),len(ver2))
        if dif:
            if len(ver1) > len(ver2):
                for i in range(dif):
                    ver2.append(0)
            else:
                for i in range(dif):
                    ver1.append(0)
        #print(ver1,ver2)
        for u,v in zip(ver1,ver2):
            u,v = int(u),int(v)
            if u > v:
                return 1
            elif v > u:
                return -1
        return 0
            
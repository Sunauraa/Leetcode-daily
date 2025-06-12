class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = defaultdict(str)
        inventory = set()
        n = len(s)
        for i in range(n):
            if m[s[i]]:
                if m[s[i]] != t[i]:
                    return False
            else:
                if t[i] in inventory:
                    return False
                m[s[i]] = t[i]
                #inventory.add(s[i])
                inventory.add(t[i])
        print(m)
        return True
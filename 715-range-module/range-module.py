class RangeModule:

    def __init__(self):
        #print(0)
        self.store = SortedList()

    def addRange(self, left: int, right: int) -> None:
        #print(1)
        #print('add',left,right)
        check = True
        for l,r in self.store:
            if left <= l <= right:
                self.store.remove((l,r))
                self.store.add((min(l,left),max(r,right)))
                check = False
        if check:
            self.store.add((left,right))

    def queryRange(self, left: int, right: int) -> bool:
        #print(2)
        #print('quert',self.store,left,right)
        l = left
        r = right
        cur = 0
        for u,v in self.store:
            if u <= l < v:
                l = min(v,r)
            elif u > l:
                return False
            if l == r:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        ski = (left == 6 and right == 56)
        #print(3)
        #print('remove',left,right,self.store)
        l = left
        r = right
        i = 0
        wowow = False
        while i < len(self.store):
            check = True
            u,v = self.store[i]
            #print(u,v)
            if l >= u and l <= v <= r:
                #print(1)
                self.store.remove((u,v))
                self.store.add((u,l))
                i+=1
                continue
            while u >= l and v <= r:
                #print(2)
                check = False
                if ski: print(u,v)
                self.store.remove((u,v))
                if i < len(self.store):
                    u,v = self.store[i]
                else:
                    wowow = True
                    break
            if wowow:
                break

            if l <= u < r and v > r:
                #print(3)
                self.store.remove((u,v))
                self.store.add((r,v))
                continue
            if u <= l and v >= r:
                #print(4)
                #print(4,self.store)
                self.store.remove((u,v))
                self.store.add((u,l))
                self.store.add((r,v))
                i+=1
                continue
            i+=1
        if ski:
            print(self.store)
            print()




# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
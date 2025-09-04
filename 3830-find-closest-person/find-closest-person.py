class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 1 + ( abs(x-z) > abs(z-y) ) - (abs(x-z) == abs(z-y))
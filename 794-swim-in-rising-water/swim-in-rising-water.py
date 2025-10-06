class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        


        heap = []
        heap.append((grid[0][0],0,0))
        n = len(grid)

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set((0,0))

        while heap:
            water, row, col = heapq.heappop(heap)

            if row == col == n-1:
                return water

            for r, c in DIRS:
                next_r = row + r
                next_c = col + c

                if next_r < 0 or next_r >= n: continue
                if next_c < 0 or next_c >= n: continue
                if (next_r, next_c) in visited: continue

                visited.add((next_r,next_c))
                next_water_level = max(grid[next_r][next_c], water)
                heapq.heappush(heap, (next_water_level, next_r, next_c))

        return -1

            

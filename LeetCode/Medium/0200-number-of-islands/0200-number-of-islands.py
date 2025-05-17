class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cnt = 0

        def DFS(r, c):
            # 예외 처리
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return
            
            # 방문 처리
            grid[r][c] = "0"
            
            # 탐색
            DFS(r-1, c)  # 위
            DFS(r, c-1)  # 왼
            DFS(r, c+1)  # 오
            DFS(r+1, c)  # 아
            
            

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    # 1 발견하면 -> DFS 로 떠넘김 -> 다 셌으면
                    DFS(r, c)  
                    # 섬 개수 증가
                    cnt += 1   

        return cnt
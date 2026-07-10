class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        ans = image[sr][sc]

        if ans == color:
            return image
            
        def dfs(i,j):
            if  i<0 or j<0 or i>=r or j>=c:
                return 
            if image[i][j] != ans:
                return
            image[i][j] = color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        dfs(sr,sc)                    
        return image
        
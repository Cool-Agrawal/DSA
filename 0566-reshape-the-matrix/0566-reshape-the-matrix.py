class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        a = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                a.append(mat[i][j])
        k = 0
        ans = []
        for i in range(r):
            ans.append([])
            for j in range(c):
                    ans[i].append(a[k])
                    k += 1
        
        return ans
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [False]*n
        def dfs(node):
            visited[node] = True
            for i in adj[node]:
                if not visited[i]:
                    dfs(i)
        dfs(source)
        return visited[destination]
         

        
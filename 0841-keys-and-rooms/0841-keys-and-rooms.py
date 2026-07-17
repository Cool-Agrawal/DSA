class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n
        def dfs(room):
            visited[room] = True
            for i in rooms[room]:
                if not visited[i]:
                    dfs(i)
        dfs(0)
        return all(visited)

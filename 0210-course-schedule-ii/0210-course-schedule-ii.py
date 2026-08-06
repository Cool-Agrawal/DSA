class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        ans = []
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i] += 1
        
        q = deque()
        for j in range(numCourses):
            if indegree[j] == 0:
                q.append(j)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                ans.append(node)
                for i in adj[node]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        
        if len(ans) == numCourses:
            return ans
        return []
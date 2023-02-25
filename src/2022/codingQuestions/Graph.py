class Graph:
    def __init__(self):
        self.adjList = {}

    def createEdge(self, start, end):
        if start in self.adjList.keys():
            self.adjList[start].append(end)
        else:
            self.adjList[start] = [end]

    def printGraph(self):
        # print(self.adjList)
        # for i in self.adjList:
        #     print(i)
        for k, v in self.adjList.items():
            print(k, " - ", ' - '.join([str(i) for i in v]))

    def bfs(self, start):
        from collections import deque
        visited = []
        queue = deque()
        queue.append(start)
        # visited.append(start)
        # print(visited)
        path=[]

        while queue:
            startnode = queue.popleft()
            path.append(startnode)
            # print(startnode, end=" ")
            # print(self.ad)

            # dictVal=self.adjList.get(startnode)
            # dictVal=[] if dictVal is None else dictVal

            for i in self.adjList.setdefault(startnode,[]):
                # print(i)
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        print(path)
    def dfs(self,start):
        from collections import deque
        visited = []
        stack = deque()
        stack.append(start)
        path=[]

        while stack:
            startnode = stack.pop()
            # print(startnode, end=" ")
            if startnode in path:
                continue
            path.append(startnode)
            for i in self.adjList.setdefault(startnode,[]):
                # print(i)
                stack.append(i)
                # print(stack)


        print(path)


g = Graph()
g.createEdge(0, 1)
g.createEdge(0, 4)
g.createEdge(1, 4)
g.createEdge(1, 3)
g.createEdge(1, 2)
g.createEdge(2, 3)
g.createEdge(3, 4)

g.bfs(0)
print()
g.dfs(0)

from collections import deque 


class Link():
    def __init__(self, name, dist) -> None:
        self.dist = dist
        self.name = name
        self.next = None


class Graph():
    def __init__(self, inputFile=None, type="undirected") -> None:
        self.adjList = []
        self.map = {}
        self.index = 0
        
        
        if type != "undirected" and type != "directed":
            type = "undirected"
        self.type = type
        if inputFile is None:
            return 
        
        try:
            f = open(inputFile, 'r')
        except FileNotFoundError:
            print (f"File {inputFile} does not exist")
            return 
            
        line = f.readline()
        line = line.strip()
        while line:
            tokens = line.split(" ")
            n1, n2, dist = tokens
            
            self.addEdge(n1, n2, dist)
            # self.addEdge(n2, n1, dist)
            
            line = f.readline()
            line = line.strip()


    def addNode(self, n):
        if n not in self.map:
            self.map[n] = self.index
            self.index += 1
            self.adjList.append(None)

    def addEdgeHelper(self, n1, n2, dist):
        self.addNode(n1)
        current = self.adjList[self.map[n1]]
        previous = current
        if current is None:
            self.adjList[self.map[n1]] = Link(n2, dist)
        else:
            while current:
                if current.name == n2:
                    current.dist = dist
                    return 
                previous = current
                current = current.next
            previous.next = Link(n2, dist)

    def addEdge(self, n1, n2, dist):
        self.addNode(n1)
        self.addNode(n2)
        self.addEdgeHelper(n1, n2, dist)

        if self.type == "undirected":
            self.addEdgeHelper(n2, n1, dist)

    def delEdgeHelper(self, n1, n2):
        current = self.adjList[self.map[n1]]
        previous = current
        while current is not None:
            if current.name == n2:
                if previous is current:
                    self.adjList[self.map[n1]] = previous.next
                else:
                    previous.next = current.next
                return 
            previous = current
            current = current.next
        print(f"Edge {n1}-{n2} does not exist")

    def delEdge(self, n1, n2):
        self.delEdgeHelper(n1, n2)
        if self.type == "undirected":
            self.delEdgeHelper(n2, n1)

    def delNode(self, n):
        pass


    def printGraph(self):
        for name in sorted(self.map.keys()):
            s = f'{name}: '
            current = self.adjList[self.map[name]]
            while current is not None:
                s = f'{s}{current.name}({current.dist}) '
                current = current.next
            print(s)


    def dfs(self, root):
        if root not in self.map:
            print(f'Node {root} does not exist in this graph')
            return 
        unvisited = dict(self.map)
        results=[]

        def dfsHelper(name):
            link = self.adjList[self.map[name]]
            del unvisited[name]
            while link is not None: 
                if link.name in unvisited:
                    print(link.name)
                    dfsHelper(link.name)
                link = link.next
                
        print(root)
        dfsHelper(root)


    def bfs(self, root):
        if root not in self.map:
            print(f'Node {root} does not exist in this graph')
            return 
        unvisited = dict(self.map)
        q = deque()
        results=[]

        q.append(root)
        del unvisited[root]

        while len(q) != 0:
            current = q.popleft()
            print(current)

            current = self.adjList[self.map[current]]
            while current is not None:
                if current.name in unvisited:
                    q.append(current.name)
                    del unvisited[current.name]
                current = current.next

    def dijkstra(self, n1):
        pass

    def topological(self, n1):
        pass


def main3():
    graph = Graph("graph.txt", "directed")
    graph.printGraph()
    graph.delEdge("A", "D")
    print()
    graph.printGraph()  
    graph.delEdge("A", "B")
    print()
    graph.printGraph()  
    graph.delEdge("A", "C")
    print()
    graph.printGraph()  
    graph.delEdge("A", "AA")
    print()
    graph.printGraph()  
    graph.delEdge("A", "AB")
    print()
    graph.printGraph()      

def main2():
    graph = Graph("graph.txta", "directed")
    graph.addEdge("A", "B", 100)
    graph.printGraph()
         
def main1():
    graph = Graph("graph.txt")
    graph.printGraph()
    print()
    graph.addEdge("A", "B", 100)
    print()
    graph.printGraph()


main1()

            
from collections import deque 
import heapq



class Link():
    def __init__(self, name, dist) -> None:
        self.dist = int(dist)
        self.name = name
        self.next = None


class Graph():
    '''Contains all graph methods'''

    def __init__(self, inputFile=None, type="undirected") -> None:
        self.adjList = []
        '''adjacency list representation. Stores each node's neighbor as link list'''
        self.map = {}
        '''map node's name to index in adjList'''
        self.index = 0
        '''Track the index of the new node in adjList'''
        
        # 
        if type != "undirected" and type != "directed":
            type = "undirected"
        self.type = type 
        '''graph is either directed or undirected'''
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
            dist = int(dist)
            
            self.addEdge(n1, n2, dist)
            
            line = f.readline()
            line = line.strip()


    def addNode(self, n):
        if n not in self.map:
            self.map[n] = self.index
            self.index += 1
            self.adjList.append(None)

    def addEdgeHelper(self, n1, n2, dist):
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

    def dijkstra(self, root):
        '''
        1. Create dijkstra node (need shortDist and parent)
        2. Initialize pq
        3. Put all nodes in pq
        4. pop from pq, iterate all its neighbors, and update short length (and pq) accordingly
        5. print or store result
        '''

        if root not in self.map:
            print(f'Node {root} does not exist in this graph')
            return 

        # Track each node's shortest dist and parent
        sp = {node: [float('inf'), None] for node in self.map.keys()}
        sp[root] = [0, root]

        visited = set()

        # [shortest dist, node name]
        pq = [(0, root)]
        heapq.heapify(pq)

        while len(pq) > 0:
            dist, node= heapq.heappop(pq)
            if node in visited:
                continue
            else:
                visited.add(node)
            
            # for each neighbor, update shortest dist if a shorter one is found
            vLink = self.adjList[self.map[node]]
            while vLink:
                if sp[vLink.name][0] > dist + vLink.dist:
                    sp[vLink.name] = [dist + vLink.dist, node]
                    heapq.heappush(pq, (sp[vLink.name][0], vLink.name))
                vLink = vLink.next

        # print result
        print("Shortest path from node", root)
        for node in self.map.keys():
            print(node, sp[node][0])

    def topological(self, n1):
        pass


def main3():
    graph = Graph("graph2.txt", "directed")
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
    graph = Graph("graph2.txt", "directed")
    graph.addEdge("A", "B", 100)
    graph.printGraph()
         
def main1():
    graph = Graph("graph1.txt", "undirected")
    graph.printGraph()
    print(graph.adjList)
    print("\n")
    graph.bfs("A")
    print("\n")
    graph.dfs("A")
    print("\n")
    graph.dijkstra("A")

main1()

            
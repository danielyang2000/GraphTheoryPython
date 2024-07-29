import pytest
from graph import Graph, Link

class TestClass:

    def test_graphInit1(self):
        g = Graph()
        assert len(g.adjList) == 0
        assert len(g.map) == 0
        assert g.index == 0

    # def test_graphInit2(self):
    #     g = Graph(type="whatisthis")
    #     assert len(g.adjList) == 0
    #     assert len(g.map) == 0
    #     assert g.index == 0

    def test_linkInit(self):
        l = Link("Bob", 100)
        assert l.name == "Bob"
        assert l.dist == 100

    def test_addNode1(self):
        g = Graph()
        g.addNode("Apple")
        assert g.map["Apple"] == 0
        assert g.index == 1
        assert len(g.adjList) == 1

        g.addNode("Bob")
        assert g.map["Bob"] == 1
        assert g.index == 2
        assert len(g.adjList) == 2

        g.addNode("Clarinet")
        assert g.map["Clarinet"] == 2
        assert g.index == 3
        assert len(g.adjList) == 3

    def test_addNode2(self):
        g = Graph()
        g.addNode("Apple")
        assert g.map["Apple"] == 0
        assert g.index == 1
        assert len(g.adjList) == 1

        g.addNode("Apple")
        assert g.map["Apple"] == 0
        assert g.index == 1
        assert len(g.adjList) == 1

        g.addNode("Apple")
        assert g.map["Apple"] == 0
        assert g.index == 1
        assert len(g.adjList) == 1

    def test_addEdge1(self):
        g = Graph()
        g.addEdge("a", "b", 100)

        vLink = g.adjList[g.map["a"]]
        assert vLink.name == "b"
        assert vLink.dist == 100

        vLink = g.adjList[g.map["b"]]
        assert vLink.name == "a"
        assert vLink.dist == 100

        g.addEdge("c", "a", 10)
        vLink = g.adjList[g.map["a"]].next
        assert vLink.name == "c"
        assert vLink.dist == 10

        vLink = g.adjList[g.map["c"]]
        assert vLink.name == "a"
        assert vLink.dist == 10

    def test_printGraph1(self, capsys):
        g = Graph()
        g.addEdge("a", "b", 100)
        g.addEdge("c", "d", 100)
        g.printGraph()
        stdout, stderr = capsys.readouterr()
        assert stdout == "a: b(100) \nb: a(100) \nc: d(100) \nd: c(100) \n"

    def test_printGraph2(self, capsys):
        g = Graph()
        g.printGraph()
        stdout, stderr = capsys.readouterr()
        assert stdout == ""

    def test_bfs1(self, capsys):
        g = Graph()
        g.addEdge("a", "b", 100)
        g.addEdge("b", "c", 100)
        g.addEdge("a", "d", 100)
        g.bfs("a")
        stdout, stderr = capsys.readouterr()
        assert stdout == "a\nb\nd\nc\n"

    def test_dfs1(self, capsys):
        g = Graph()
        g.addEdge("a", "b", 100)
        g.addEdge("b", "c", 100)
        g.addEdge("a", "d", 100)
        g.dfs("a")
        stdout, stderr = capsys.readouterr()
        assert stdout == "a\nb\nc\nd\n"

    def test_dijkstra1(self, capsys):
        graph = Graph("graph1.txt", "directed")
        graph.dijkstra("A")
        stdout, stderr = capsys.readouterr()
        out = stdout.split("\n")

        assert out[0] == "Shortest path from node A"
        assert out[1] == "A 0"
        assert out[2] == "B 2"
        assert out[3] == "D 12"
        assert out[4] == "C 5"
        assert out[5] == "Z 1"

    def test_dijkstra2(self, capsys):
        graph = Graph("graph1.txt", "undirected")
        graph.dijkstra("A")
        stdout, stderr = capsys.readouterr()
        out = stdout.split("\n")

        assert out[0] == "Shortest path from node A"
        assert out[1] == "A 0"
        assert out[2] == "B 2"
        assert out[3] == "D 12"
        assert out[4] == "C 5"
        assert out[5] == "Z 1"






        

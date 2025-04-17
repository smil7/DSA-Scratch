class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            print("Already in the graph")
            return
        self.adjacentList[node] = []
        self.number_of_nodes += 1

    def addEdge(self, node1, node2):
        if (node1 and node2) in self.adjacentList:
            if node2 in self.adjacentList[node1]:
                print(f"Found an edge between {node1} and {node2}")
                return
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
        else:
            print(f"Node {node1} is not found!")

    def showConnections(self):
        all_nodes = self.adjacentList.keys()
        for node in all_nodes:
            node_connections = self.adjacentList[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(f"{node} ---> {connections}")

graph = Graph()
graph.addVertex('0')
graph.addVertex('1')
graph.addVertex('2')
graph.addVertex('3')
graph.addVertex('4')
graph.addVertex('5')
graph.addVertex('6')
graph.addEdge('3', '1')
graph.addEdge('3', '4')
graph.addEdge('4', '2')
graph.addEdge('4', '5')
graph.addEdge('1', '2')
graph.addEdge('1', '0')
graph.addEdge('2', '1')
graph.addEdge('0', '2')
graph.addEdge('6', '5')

graph.showConnections()
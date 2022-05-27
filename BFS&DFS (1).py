# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DFS(self, v):

		# Create a set to store visited vertices
		visited = set()

		# Call the recursive helper function
		# to print DFS traversal
		self.DFSUtil(v, visited)

	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		# and print it
		visited.add(v)
		print(v, end=' ')

		# Recur for all the vertices
		# adjacent to this vertex
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)


	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print (s, end = " ")

			# Get all adjacent vertices of the
			# dequeued vertex s. If a adjacent
			# has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

# Driver code

# Create a graph given in
# the above diagram
g = Graph()
print("Enter no.of nodes:")
N=int(input())
S=int(N*(N-1)/2)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
for i in range(0,S,1):
    print("Edge is present between nodes:")
    n1=int(input("First node:"))
    n2=int(input("Second node:"))
    g.addEdge(n1,n2)

# print ("Following is Breadth First Traversal"
# 				" (starting from vertex 2)")
# g.BFS(2)
rep='y'
while rep=='y':
	print("Which method do you want to choose?")
	print("1.DFS")
	print("2.BFS")
	ch=int(input())
	if ch==1:
		print("Following is DFS (starting from vertex 2)")
		g.DFS(2)
	elif ch==2:
		print("Following is BFS traversal (starting from vertex 2)")
		g.BFS(2)
	print("\n")
	print("Do you want to continue ?")
	rep=input()

# This code is contributed by Neelam Yadav

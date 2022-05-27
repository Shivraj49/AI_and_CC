
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

visited=set() # Maintaining the set of visited nodes

def dfsSearch (visited,graph,node):
    if node not in visited:
        print (node,end=' ')
        visited.add(node)
    for nigh in graph[node]:
        dfsSearch(visited,graph,nigh)
        
#Main Function      
print(" Following is the Depth-First Search")
dfsSearch(visited,graph,'5')
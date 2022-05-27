
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
#BFS
visited=[]
queue=[]

def bfs (visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while(queue):
        m=queue.pop(0)
        print(m,end =' ')
    
        for neigh in graph[m]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
           
#DFS
visitedd=set() # Maintaining the set of visited nodes

def dfsSearch (visitedd,graph,node):
    if node not in visitedd:
        print (node,end=' ')
        visitedd.add(node)
    for nigh in graph[node]:
        dfsSearch(visitedd,graph,nigh)
    
             
flag=True
while (flag):
    print("Select Your Operation (1.BFS) (2.DFS)")
    argument=int(input())
    if (argument == 1):
        bfs (visited, graph, '5')
        
    elif (argument == 2):
        dfsSearch(visitedd,graph,'5')
        
    print("Do you want to continue (yes or no)")
    cont=input()
    if (cont == 'yes'):
        flag=True
    else:
        flag= False
        print("Thank You")

       

            



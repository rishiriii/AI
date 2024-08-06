graph={
       'A':['B','C','D'],
       'B':['A','C'],
       'C':['A','B','E'],
       'D':['A'],
       'E':['C']
       }
visited=[]
queue=[]
def bfs(visited,graph,node):
       visited.append(node)
       queue.append(node)
       while queue:
              s=queue.pop(0)
              print(s,end=" ")
              for neighbor in graph[s]:
                     if neighbor not in visited:
                            visited.append(neighbor)
                            queue.append(neighbor)
bfs(visited,graph,'A')

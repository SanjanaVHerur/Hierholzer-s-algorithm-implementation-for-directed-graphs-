# global graph
# global path 
# global n 
graph={}
path1=[]
n=0

def add_vertex(v):
    global graph
    global path 
    global n
    if v in graph:
        print("Vertex",v,"already exists")
    else:
        n = n + 1
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print("Vertex",v1,"does not exist")
    elif v2 not in graph:
        print("Vertex",v2,"does not exist")
    else:
        graph[v1].append(v2)

def print_graph():
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex,"->",edges)

def cir():
    for i in range(n):
        if(indeg[i]!=outdeg[i]):
            return 0
    return 1

def path():
    k=0
    l=0
    for i in range(n):
        if(indeg[i]!=outdeg[i]):
            if(outdeg[i]-indeg[i]==1):
                k=k+1
            elif(indeg[i]-outdeg[i]==1):
                l=l+1
            elif(indeg[i]-outdeg[i]>1 or indeg[i]-outdeg[i]<1):
                return 0
    if(k==1 and l==1):
        return 1

def findstartnode():
    start = 0
    for i in range(n):
        if(indeg[i]!=outdeg[i] and outdeg[i]>0): 
            start = i
    return start

def dfs(at):
    while(outdeg[at]!=0):
        outdeg[at]=outdeg[at]-1
        next_edge = graph.get(at,outdeg[at])
        dfs(next_edge[outdeg[at]])
    path1.insert(0,at)

# def eulpath():
#     dfs(findstartnode())
#     if path.size==6:
#         return path
#     return 0


def findeul():
    if cir()==1:
        dfs(0)
    elif path()==1:
        dfs(findstartnode())
    else:
        print("\nNo euler path or circuit exists")
        exit()

#Driver Code

add_vertex(0)
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1,0)
add_edge(0,3)
add_edge(3,4)
add_edge(4,0)
add_edge(0,2)
add_edge(2,1)

# graph example for no euler path or circuit
# add_edge(0,2)
# add_edge(2,1)
# add_edge(3,2)
# add_edge(2,4)

indeg = [0]*n
outdeg = [0]*n

for vertex in graph:
    for edges in graph[vertex]:
        outdeg[vertex]=0
        indeg[edges]=0

for vertex in graph:
    for edges in graph[vertex]:
        outdeg[vertex]=outdeg[vertex]+1
        indeg[edges]=indeg[edges]+1

findeul()
m=len(path1)
if(path1[0]==path1[m-1]):
    print("\nEuler circuit exists")
else:
    print("Euler path exists\n")
for i in range(len(path1)):
    print(path1[i]," ",end="")
print("\n")
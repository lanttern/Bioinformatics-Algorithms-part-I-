
with open ('6_4.txt') as r:
    source = int((r.readline()).translate(None, '\n'))
    sink = int((r.readline()).translate(None, '\n'))
    graph = {}
    weight = {}
    t = []
    for line in r:
        temp = line.translate(None, '\n')
        temp = temp.replace ('->', ' ')
        temp = temp.replace (':', ' ')
        temp = temp.split()
        t.append(temp)
    #print t
    for element in t:
        #print element, graph
        if int(element[0]) not in graph:
           graph[int(element[0])] = [int(element[1])]
        if int(element[0]) in graph and int(element[1]) not in graph[int(element[0])]:
           graph[int(element[0])] += [int(element[1])]
        weight[element[0] + element[1]] = int(element[2])

#print source, sink, graph, weight
import networkx as nx
def find_path(graph, start, end, path=[]):
        path = path + [start]
        #print path, start
        if start == end:
            return path
        if not graph.has_key(start):
            path += [end]
            return path
        for node in graph[start]:
            if node not in path:
                path += find_path(graph, node, end, path)
        return sorted(set(path))
def longest_path(G, weight, source, sink):
    dist = {} # stores [node, distance] 
    
   # nodes = nx.topological_sort(G)
    
    source_to_sink = find_path(graph, source, sink, path=[])
    #print 'iiii'
    print source_to_sink
    for node in G.nodes():
        if node not in source_to_sink:
            G.remove_node(node)
    #print list(G)
    for node in source_to_sink:
        # pairs of dist,node for all incomingif edges
       # G.pred[source] = {}
        #print node, G.pred[node]
        pairs = [(dist[v][0]+weight[str(v) + str(node)],v) for v in G.pred[node]] 
        if pairs:
            dist[node] = max(pairs)
            
            #l += dist[node]
        else:
            dist[node] = (0, node)
        
    length, node  = dist[sink]
    l = length
    path = [sink]
    while length > 0:
        path.append(node)
        length,node = dist[node]
    
    return l, list(reversed(path))
'''
if __name__=='__main__':
    G = nx.DiGraph()
    G.add_path([1,2,3,4])
    G.add_path([1,20,30,31,32,4])
#    G.add_path([20,2,200,31])
'''
#g = {0: [1, 2], 1: [4], 2: [3], 3: [4]}
#weight = {'01':7, '02':4, '14': 1, '23': 2, '34': 3}
G = nx.DiGraph(graph)
length, p = longest_path(G, weight, source, sink)
print length
path = ''
for e in p:
    path += str(e) + '->'
print path[:-2]
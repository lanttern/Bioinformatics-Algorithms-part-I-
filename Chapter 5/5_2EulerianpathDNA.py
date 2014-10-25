# -*- coding: utf-8 -*-
"""
CODE CHALLENGE: Solve the Eulerian Path Problem.
     Input: The adjacency list of a directed graph that has an Eulerian path.
     Output: An Eulerian path in this graph.

Sample Input:
     0 -> 2
     1 -> 3
     2 -> 1
     3 -> 0,4
     6 -> 3,7
     7 -> 8
     8 -> 9
     9 -> 6

Sample Output:
     6->7->8->9->6->3->0->2->1->3->4
@author: zhihuixie
"""
import networkx as nx
graph = {}
with open ('5_2.txt') as r:
    for line in r:
        line = line.translate(None, '\n')
        line = line.replace(' -> ', ' ')
        line = line.replace(',', ' ')
        line = line.split()
        temp = []
        for i in range (1, len(line)):
            temp.append(line[i])
            graph[line[0]] = temp
#print graph
#graph ={0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]} 
G = nx.DiGraph(graph)
def Allpath(G, node):
    g = G.__class__(G)
    v = node
    while g.size() > 0:
        n = v  
        #if g.edges(n) == []:
         #   break
        # sort nbrs here to provide stable ordering of alternate cycles
        nbrs = sorted([v for u,v in g.edges(n)])
        for v in nbrs:
            g.remove_edge(n,v)
            bridge = not nx.is_connected(g.to_undirected())
            #print bridge
            if bridge:
                g.add_edge(n,v)  # add this edge back and try another
            else:
                break  # this edge is good, break the for loop 
        if bridge:
            g.remove_edge(n,v)            
            g.remove_node(n)
        yield (n,v)
def EulerPath(G):
    nodes = list(G.nodes_iter())
    for node in nodes:
        if G.in_degree(node) < G.out_degree(node):
           print node, G.in_degree(node), G.out_degree(node)
           path = list(Allpath(G, node))
           #if len(path) == G.size():
           cycle = path[0][0]
           for edge in path:
               cycle += edge[-1][-1]
           print cycle
           break
EulerPath(G)
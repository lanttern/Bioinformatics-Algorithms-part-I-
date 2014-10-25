# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:55:29 2013
CODE CHALLENGE: Solve the Eulerian Cycle Problem.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

Sample Input:
     0 -> 3
     1 -> 0
     2 -> 1,6
     3 -> 2
     4 -> 2
     5 -> 4
     6 -> 5,8
     7 -> 9
     8 -> 7
     9 -> 6

Sample Output:
     6->8->7->9->6->5->4->2->1->0->3->2->6
@author: zhihuixie
"""
import networkx as nx
graph = {}
with open ('5_5.txt') as r:
    for line in r:
        line = line.translate(None, '\n')
        line = line.replace(' -> ', ' ')
        line = line.replace(',', ' ')
        line = line.split()
        temp = []
        for i in range (1, len(line)):
            temp.append(int(line[i]))
            graph[int(line[0])] = temp
            
graph ={0:[2],1:[3],2:[1],3:[0,4],6:[3,7],7:[8],8:[9],9:[6]} 
G = nx.DiGraph(graph)
def test(G, node):
    g = G.__class__(G)
    v = node
    while g.size() > 0:
        n = v  
        #print n
        if g.edges(n) == []:
            break
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

nodes = list(G.nodes_iter())
path = [(1, 1)]
for node in nodes: 
    path = list(test(G, node))
    if len(path) == G.size():
       print path

cycle = str(path[0][0]) + '->'
for edge in path:
    cycle += str(edge[-1]) + '->'
#print cycle[:-2]
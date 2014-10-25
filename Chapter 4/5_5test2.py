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
            
graph ={0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]} 
G = nx.DiGraph(graph)
#print G
a = list(nx.eulerian_circuit(G))
cycle = str(a[0][0]) + '->'
for edge in a:
    cycle += str(edge[-1]) + '->'
print cycle[:-2]

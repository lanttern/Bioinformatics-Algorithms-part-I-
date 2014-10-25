# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 21:45:55 2013
As the question on the preceding step illustrates, not every Eulerian path in the paired de Bruijn graph constructed from (k,d)-mer composition spells out a solution of the String Reconstruction from Read-Pairs Problem.

CODE CHALLENGE: Solve the String Reconstruction from Read-Pairs Problem.
     Input: An integer d followed by a collection of paired k-mers PairedReads.
     Output: A string Text with (k, d)-mer composition equal to PairedReads.

Sample Input:
     2
     GAGA|TTGA
     TCGT|GATG
     CGTG|ATGT
     TGGT|TGAG
     GTGA|TGTT
     GTGG|GTGA
     TGAG|GTTG
     GGTC|GAGA
     GTCG|AGAT

Sample Output:
     GTGGTCGTGAGATGTTGA

@author: zhihuixie
"""
import networkx as nx
with open('5_4.txt') as r:
    d = int((r.readline()).translate(None, '\n'))
    array = []
    for line in r:
        s = line.translate(None, '\n')
        array.append(s)
    k = (len(array[0]) -1)/2 
print k
def Graph(array, k):
    graph = {}   
    for string in array:
        prefix = string[0:k-1] + string[k] + string[k+1:2*k]
        suffix = string[1:k] + string[k] + string[k+2:]
        graph[prefix] = [suffix]
    return graph
l = len(Graph(array, k))
print l
G = nx.DiGraph(Graph(array, k))
def Allpath(G, node):
    g = G.__class__(G)
    #print g.edges()
    v = node
    while g.size() > 0:
        n = v  
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
def EulerPath(G):
    nodes = list(G.nodes_iter())
    for node in nodes:
        if G.in_degree(node) < G.out_degree(node):
           print node, G.in_degree(node), G.out_degree(node)
           path = list(Allpath(G, node))
           break
    string = path[0][0][:k-1]
    for i in range (0, len(path)):
        string += path[i][1][k-2]
    for j in range(l-k-d, len(path)):
        string += path[j][1][-1]
    print string

EulerPath(G)
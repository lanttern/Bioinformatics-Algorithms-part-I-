# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:50:20 2013

DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

CODE CHALLENGE: Solve the de Bruijn Graph from k-mers Problem.

Sample Input:
     GAGG
     GGGG
     GGGA
     CAGG
     AGGG
     GGAG

Sample Output:
     AGG -> GGG
     CAG -> AGG
     GAG -> AGG
     GGA -> GAG
     GGG -> GGA,GGG
@author: zhihuixie
"""

from Covertdict import Covert

with open ('5_4.txt') as r:
    DNA_array = []
    for line in r:
        line = line.translate(None, '\n')
        DNA_array.append(line)

#DNA_array = ['GAGG', 'GGGG', 'GGGA', 'CAGG', 'AGGG', 'GGAG']
def find_nodes(DNA_array):
    nodes = []
    for DNA in DNA_array:
        if DNA[0:len(DNA)-1] not  in nodes:
                nodes.append(DNA[0:len(DNA)-1])
        if DNA[1:] not  in nodes:
                nodes.append(DNA[1:])
    return nodes
def DeBruijnGraph(nodes):
    copy = list(nodes)
    pattern = {}
    for node in nodes:
        temp = []
        for nodecopy in copy:
            if node[1:] == nodecopy[:-1] and nodecopy not in temp and node + nodecopy[-1] in DNA_array:
                temp.append(nodecopy)
                pattern[node] = temp
    order_pattern = Covert([item for item in pattern])
    for element in order_pattern:
        print element + ' -> '+ str(pattern[element])
nodes = find_nodes(DNA_array)
#print nodes
DeBruijnGraph(nodes)
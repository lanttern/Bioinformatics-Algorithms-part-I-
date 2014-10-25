# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie
CODE CHALLENGE: Solve the Trie Construction Problem.
     Input: A collection of strings Patterns.
     Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has
     n nodes, first label the root with 1 and then label the remaining nodes with the integers 2 through n in
     any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first
     two members of the triple must be the integers labeling the initial and terminal nodes of the edge,
     respectively; the third member of the triple must be the symbol labeling the edge.

Sample Input:
     GGTA
     CG
     GGC

Sample Output:
     1 2 G
     2 3 G
     3 4 T
     4 5 A
     3 6 C
     1 7 C
     7 8 G
"""
patterns = []
with open("8_1.txt") as r:
    for line in r:
        patterns.append(line.translate(None, "\n"))


patterns = ["GGTA", "GGC", "CG"]

l = sum([len(i) for i in patterns])

#l = len(pattern)
def TirePattern (patterns, l):
    tires = [dict() for x in range(l)]
    end = 1
    
    for pattern in patterns:
       start = 0 
       for s in pattern:
         if s in tires[start]:
             start = tires[start][s]
         else:
             print start + 1, end + 1, s
             tires[start][s] = end
             start = end
             end += 1
             #print start, end, s
             #start = end
        

    print tires
TirePattern (patterns, l)

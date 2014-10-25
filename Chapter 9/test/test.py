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
from suffix_tree import SuffixTree
s = "AAAAAAEWSSDE"
tree = SuffixTree (s)

for l in tree.leaves:
    print l.pathLabel

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:01:44 2014

@author: zhihuixie
Longest Repeat Problem: Find the longest repeat in a string.
     Input: A string Text.
     Output: A longest repeat in Text, i.e., a longest substring of Text that appears in Text more than once.

CODE CHALLENGE: Solve the Longest Repeat Problem.

Sample Input:
     ATATCGTTTTATCGTT

Sample Output:
     TATCGTT

"""
from suffix_tree1 import SuffixTree, print_node
with open("8_4.txt") as r:
    s = (r.readline()).translate(None, "\n")
    #t = (r.readline()).translate(None, "\n")
#s = "ATAAATG$" 

tree = SuffixTree(s)
print_node(tree.root, tree.buff)
#print a
#t = "CATGCTGGGCTGGCT"

# -*- coding: utf-8 -*-
"""
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.
     Input: A string Text.
     Output: BWT(Text).

CODE CHALLENGE: Solve the Burrows-Wheeler Transform Construction Problem.

Sample Input:
     GCGTGCCTGGTCA$

Sample Output:
     ACTGGCT$TGCGGC

"""
#from suffix_tree1 import SuffixTree, print_node
with open("7_1.txt") as r:
    s = (r.readline()).translate(None, "\n")
    #t = (r.readline()).translate(None, "\n")
#s = "GCGTGCCTGGTCA$" 

def Cycle (s):
    array = [s]
    l = len(s)
   # print l
    i = 1
    while i < l:
       temp = s[l-i:] + s[:l-i] 
       array.append(temp)
       i += 1
    return sorted(array)
print ''.join(a[-1] for a in Cycle (s))
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
from suffix_tree1 import SuffixTree
with open("8_5.txt") as r:
    s = (r.readline()).translate(None, "\n")
    t = (r.readline()).translate(None, "\n")
#s = "TCGGTAGATTGCGCCCACTC"
#t = "AGGGGCTCGCAGTGTAAGAA"

tree = SuffixTree (s)
print tree()
tree.add(t)
common_substring = tree.common_substring(2)
max_length = 0
for (a, b) in common_substring:
    if a in s and a in t:
        if len(a) >= max_length:
            max_length  = len(a)
            longest_common_substring = a
            
print longest_common_substring
#print a
#index_sub = set(index_substring)
#print s[index_substring[0]:index_substring[1]]

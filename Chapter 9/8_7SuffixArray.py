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
#from suffix_tree1 import SuffixTree
with open("8_7.txt") as r:
    s = (r.readline()).translate(None, "\n")
    #t = (r.readline()).translate(None, "\n")
s = "AACGATAGCGGTAGA$" 
#t = "CATGCTGGGCTGGCT"
#tree = SuffixTree (s)
#c = {"A":1, "C":2, "G":3, "T":4, "$":0}
#print len(s)
#array = {}
key=lambda x: s[x:x + 1000] 
a = sorted([key(i) for i in range(len(s))]) 
#print a
b = [s.index(el) for el in a]

print b


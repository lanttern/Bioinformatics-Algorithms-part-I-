# -*- coding: utf-8 -*-
"""
CODE CHALLENGE: Construct a partial suffix array.
     Input: A string Text and a positive integer K.
     Output: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty
     entries in the partial suffix array.

Sample Input:
     PANAMABANANAS$
     5

Sample Output:
     1,5
     11,10
     12,0

"""
#from suffix_tree1 import SuffixTree
with open("7_5.txt") as r:
    s = (r.readline()).translate(None, "\n")
    k = int((r.readline()).translate(None, "\n"))
    #t = (r.readline()).translate(None, "\n")
#s = "PANAMABANANAS$" 
#t = "CATGCTGGGCTGGCT"
#tree = SuffixTree (s)
#c = {"A":1, "C":2, "G":3, "T":4, "$":0}
#print len(s)
#array = {}
key=lambda x: s[x:x + 1000] 
a = sorted([key(i) for i in range(len(s))]) 
#print a
#b = [s.index(el) for el in a]
for i in range(0, len(a)):
    if s.index(a[i]) % k == 0:
       print i, s.index(a[i])
#print b

